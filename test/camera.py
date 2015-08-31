__author__ = 'Su Lei'

import vtk

def far(obj, ev):
    global ren, i, renWin
    camera2 = ren.GetActiveCamera()
    camera2.SetPosition(1.0, 1.0, i)
    ren.SetActiveCamera(camera2)
    renWin.Render()
    i += 1
    print i

i = 1
sphere = vtk.vtkSphereSource()
sphere.SetCenter(1.0, 1.0, -1.0)
sphere.SetRadius(1.0)
sphere.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(sphere.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
print actor.GetBounds(), actor.GetPosition(), actor.GetCenter()
ren = vtk.vtkRenderer()
ren.AddActor(actor)


camera1 = ren.GetActiveCamera()
camera1.SetPosition(1.0, 1.0, 1.0)
camera1.SetFocalPoint(1.0, 1.0, 0.0)
camera1.SetViewUp(0.0, 1.0, 0.0)
camera1.SetViewAngle(60.0)
ren.SetActiveCamera(camera1)

bounds = actor.GetBounds()
print bounds


renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
sytle = vtk.vtkInteractorStyleSwitch()
iren.SetInteractorStyle(sytle)
# iren.RemoveObservers('LeftButtonPressEvent')
# iren.AddObserver('LeftButtonPressEvent', far, 1.0)
renWin.Render()
iren.Initialize()
iren.Start()
