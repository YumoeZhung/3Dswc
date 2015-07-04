__author__ = 'Su Lei'


import vtk

cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(10)

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor)
ren1.SetBackground(0.1, 0.2, 0.4)

renWindow = vtk.vtkRenderWindow()
renWindow.AddRenderer(ren1)
renWindow.SetSize(300, 300)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWindow)

for i in xrange(360):
    renWindow.Render()
    ren1.GetActiveCamera().Yaw(10)

interactor.Initialize()
interactor.Start()




