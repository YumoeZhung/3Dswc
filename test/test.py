import vtk

t1 = 0
t2 = 0
t3 = 0
iren = vtk.vtkRenderWindowInteractor()

def pickerfunc (object, event):
    if event == 'LeftButtonPressEvent':
        print 'DOK'
        print t1
   
    if event == 'LeftButtonReleaseEvent':
        print 'ROK'
        print t2

    if event == 'RightButtonPressEvent':
        print t3
    iren.RemoveObserver (t1)
    iren.RemoveObserver (t2)
    iren.RemoveObserver (t3)
   

def main():
    cone = vtk.vtkConeSource()
    cone.SetHeight( 3.0 )
    cone.SetRadius( 1.0 )
    cone.SetResolution( 10 )

    map = vtk.vtkPolyDataMapper()
    map.SetInputConnection(cone.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(map)

    ren = vtk.vtkRenderer()
    ren.AddActor(actor)
    ren.SetBackground(0.1, 0.2, 0.4)

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(300, 300)

    iren.SetRenderWindow(renWin)
    style = vtk.vtkInteractorStyleTrackballCamera()
    iren.SetInteractorStyle(style)
   
    global t1
    global t2
    global t3
    t1 = iren.AddObserver ("LeftButtonPressEvent", pickerfunc)
    t2 = iren.AddObserver ("LeftButtonReleaseEvent", pickerfunc)
    t3 = iren.AddObserver ("RightButtonPressEvent", pickerfunc)

    iren.Initialize()
    iren.Start()

if __name__ == "__main__":
    main()