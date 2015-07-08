import vtk
from vtk import *

#setup points and vertices
Points = vtk.vtkPoints()
Triangles = vtk.vtkCellArray()

Points.InsertNextPoint(1.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 0.0, 0.0)
Points.InsertNextPoint(0.0, 1.0, 0.0)

Triangle = vtk.vtkTriangle()
Triangle.GetPointIds().SetId(0, 0)
Triangle.GetPointIds().SetId(1, 1)
Triangle.GetPointIds().SetId(2, 2)
Triangles.InsertNextCell(Triangle)

#setup colors
Colors = vtk.vtkUnsignedCharArray()
Colors.SetNumberOfComponents(3)
Colors.SetName("Colors")
Colors.InsertNextTuple3(255, 0, 0)
Colors.InsertNextTuple3(0, 255, 0)
Colors.InsertNextTuple3(0, 0, 255)

polydata = vtk.vtkPolyData()
polydata.SetPoints(Points)
polydata.SetPolys(Triangles)

polydata.GetPointData().SetScalars(Colors)


mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polydata)

#create the actor with the mapper
actor = vtk.vtkActor()
actor.SetMapper(mapper)

ren = vtk.vtkRenderer()
iren = vtk.vtkRenderWindowInteractor()
renWin = vtk.vtkRenderWindow()
#add the actor to the display
ren.AddActor(actor)
iren.SetRenderWindow(renWin)

# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()