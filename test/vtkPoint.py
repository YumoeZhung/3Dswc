__author__ = 'Su Lei'


import vtk

def reRender(obj, env):
    print 'hhhh'
    points1 = [
        [0, 0.3, 0],
        [0.1, 0, 0]
    ]

    vtk_points1 = vtk.vtkPoints()
    vtk_points_cells1 = vtk.vtkCellArray()

    vtk_points1.InsertPoint(0, points1[0])
    vtk_points1.InsertPoint(1, points1[1])
    vtk_points_cells1.InsertNextCell(2, [0, 1])

    vtk_vertices1 = vtk.vtkPolyData()
    vtk_vertices1.SetPoints(vtk_points1)
    vtk_vertices1.SetVerts(vtk_points_cells1)

    vtk_mapper1 = vtk.vtkPolyDataMapper()
    vtk_mapper1.SetInputData(vtk_vertices1)

    vtk_actor1 = vtk.vtkActor()
    vtk_actor1.GetProperty().SetPointSize(10)
    vtk_actor1.SetMapper(vtk_mapper1)

    ren.AddActor(vtk_actor1)
    renWin.Render()


def test(obj, env):
    print 'ssss'



points = [
    [0, 0.5, 0],
    [0.4, 0, 0]
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
renWin.SetPointSmoothing(1)

iren = vtk.vtkRenderWindowInteractor()
iren.RemoveObservers('StartPickEvent')
iren.AddObserver('StartPickEvent', test, 1.0)
ren.AddActor(vtk_actor)
renWin.AddRenderer(ren)
iren.SetRenderWindow(renWin)

renWin.Render()


iren.Start()