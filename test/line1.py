import vtk

p_array = [
           [0, 0, 0],
           [1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]
           ]

points = vtk.vtkPoints()
cells = vtk.vtkCellArray()

for i in xrange(len(p_array)):
    points.InsertPoint(i, p_array[i])

cells.InsertNextCell(4, [0, 1, 2, 3])

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

pointColors = vtk.vtkUnsignedCharArray()
pointColors.SetNumberOfComponents(3)
pointColors.InsertNextTupleValue(red)                    
pointColors.InsertNextTupleValue(green)         
pointColors.InsertNextTupleValue(red)         
pointColors.InsertNextTupleValue(green)         


linePolyData = vtk.vtkPolyData()
linePolyData.SetPoints(points)
linePolyData.SetLines(cells)

# linePolyData.SetVerts(cells)
linePolyData.GetPointData().SetScalars(pointColors)



lineMapper = vtk.vtkPolyDataMapper()
lineMapper.SetInputData(linePolyData)

lineActor = vtk.vtkActor()
lineActor.SetMapper(lineMapper)
lineActor.GetProperty().SetLineWidth(10)

ren = vtk.vtkRenderer()
ren.AddActor(lineActor)
ren.SetBackground(0, 0, 0)

renWin = vtk.vtkRenderWindow()
renWin.SetSize(300, 300)
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()