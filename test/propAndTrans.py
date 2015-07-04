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
coneActor.GetProperty().SetColor(0.2, 0.63, 0.79)
coneActor.GetProperty().SetDiffuse(0.7)
coneActor.GetProperty().SetSpecular(0.4)
coneActor.GetProperty().SetSpecularPower(20)

property1 = vtk.vtkProperty()
property1.SetColor(1.0, 0.3882, 0.2784)
property1.SetDiffuse(0.7)
property1.SetSpecular(0.4)
property1.SetSpecularPower(20)

coneActor2 = vtk.vtkActor()
coneActor2.SetMapper(coneMapper)
coneActor2.GetProperty().SetColor(0.2, 0.63, 0.79)
coneActor2.SetProperty(property1)
coneActor2.SetPosition(0, 6, 0)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor)
ren1.AddActor(coneActor2)
ren1.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

interactor1 = vtk.vtkRenderWindowInteractor()
interactor1.SetRenderWindow(renWin)
interactor1.Initialize()
interactor1.Start()


ren1 = vtk.vtkRenderer()
ren1.SetBackground(0.1, 0.2, 0.4)
