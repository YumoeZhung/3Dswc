__author__ = 'Su Lei'

import vtk

arrowSource = vtk.vtkArrowSource()
arrowMapper = vtk.vtkPolyDataMapper()
arrowMapper.SetInputConnection(arrowSource.GetOutputPort())

arrowActor = vtk.vtkActor()
arrowActor.SetMapper(arrowMapper)

ren = vtk.vtkRenderer()
ren.AddActor(arrowActor)
ren.SetBackground(0.1, 0.2, 0.3)

renWin = vtk.vtkRenderWindow()
renWin.SetSize(300, 300)
renWin.AddRenderer(ren)

interactor1 = vtk.vtkRenderWindowInteractor()
interactor1.SetRenderWindow(renWin)

renWin.Render()
interactor1.Start()
