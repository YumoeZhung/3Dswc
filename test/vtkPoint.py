__author__ = 'Su Lei'


import vtk

points = [
    [0, 0, 0],
    [1, 0, 0]
]

vtk_points = vtk.vtkPoints()
vtk_points_cells = vtk.vtkCellArray()

vtk_points.InsertPoint(0, points[0])
vtk_points.InsertPoint(1, points[1])
vtk_points_cells.InsertNextCell(2, [0, 1])

vtk_vertices = vtk.vtkPolyData()
vtk_vertices.SetPoints(vtk_points)
vtk_vertices.SetVerts(vtk_points_cells)

vtk_mapper = vtk.vtkPolyDataMapper()
vtk_mapper.SetInputData(vtk_vertices)

vtk_actor = vtk.vtkActor()
vtk_actor.GetProperty().SetPointSize(10)
vtk_actor.SetMapper(vtk_mapper)

ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
iren = vtk.vtkRenderWindowInteractor()

ren.AddActor(vtk_actor)
renWin.AddRenderer(ren)
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()