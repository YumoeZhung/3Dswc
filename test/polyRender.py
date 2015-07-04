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
ren1.SetViewport(0.0, 0.0, 0.5, 1.0)

ren2 = vtk.vtkRenderer()
ren2.AddActor(coneActor)
ren2.SetBackground(0.2, 0.3, 0.5)
ren2.SetViewport(0.5, 0.0, 1.0, 1.0)

renWind = vtk.vtkRenderWindow()
renWind.AddRenderer(ren1)
renWind.AddRenderer(ren2)
renWind.SetSize(600, 300)

# ren1.ResetCamera()
# ren1.GetActiveCamera().Azimuth(90)

renWind.Render()

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWind)

interactor.Initialize()
interactor.Start()
# for i in xrange(360):
#     renWind.Render()
#     ren1.GetActiveCamera().Azimuth(1)
#     ren2.GetActiveCamera().Azimuth(1)


