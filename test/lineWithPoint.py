import vtk

points = [
          [0, 0, 0],
          [0, 1, 0],
          [1, 0, 0]
          ]

vtk_points = vtk.vtkPoints()
for i in xrange(len(points)):
    vtk_points.InsertPoint(i, points[i])

lines_cell_array = vtk.vtkCellArray()
lines_cell_array.InsertNextCell(3, [0, 1, 2])

vertice_cell_array = vtk.vtkCellArray()
vertice_cell_array.InsertNextCell(3, [0, 1, 2])

lines_show = vtk.vtkPolyData()
lines_show.SetPoints(vtk_points)
lines_show.SetLines(lines_cell_array)

lines_mapper = vtk.vtkPolyDataMapper()
lines_mapper.SetInputData(lines_show)

lines_actor = vtk.vtkActor()
lines_actor.SetMapper(lines_mapper)
lines_actor.GetProperty().SetLineWidth(5)

vertices_show = vtk.vtkPolyData()
vertices_show.SetPoints(vtk_points)
vertices_show.SetVerts(vertice_cell_array)

vertices_mapper = vtk.vtkPolyDataMapper()
vertices_mapper.SetInputData(vertices_show)

vertices_actor = vtk.vtkActor()
vertices_actor.SetMapper(vertices_mapper)
vertices_actor.GetProperty().SetPointSize(20)

ren = vtk.vtkRenderer()
ren.AddActor(lines_actor)
ren.AddActor(vertices_actor)
ren.SetBackground(0.1, 0.2, 0.3)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()