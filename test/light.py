__author__ = 'Su Lei'

import vtk

sphere = vtk.vtkSphereSource()
sphere.SetThetaResolution(100)
sphere.SetPhiResolution(50)

sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphere.GetOutputPort())

sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)
sphereActor.GetProperty().SetColor(1, 0, 0)
sphereActor.GetProperty().SetAmbient(0.3)
sphereActor.GetProperty().SetDiffuse(0.0)
sphereActor.GetProperty().SetSpecular(0.5)

ren1 = vtk.vtkRenderer()
ren1.AddActor(sphereActor)
ren1.SetBackground(0.1, 0.2, 0.4)

light1 = vtk.vtkLight()
light1.SetFocalPoint(0, 0, 0)
light1.SetPosition(-0.8, 0.8, 1)
ren1.AddLight(light1)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

# for i in xrange(334):
#     sphereActor.GetProperty().SetAmbient(i * 0.03)
#     renWin.Render()

def Lighting(obj, ev):
    global i
    i += 1
    if i > 10:
        i = 0
    sphereActor.GetProperty().SetSpecularPower(i)
    renWin.Render()

i = 0
interactor1 = vtk.vtkRenderWindowInteractor()
interactor1.SetRenderWindow(renWin)
interactor1.RemoveObservers('LeftButtonPressEvent')
interactor1.AddObserver('LeftButtonPressEvent', Lighting, 1.0)
interactor1.Initialize()
interactor1.Start()



