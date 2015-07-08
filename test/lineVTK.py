__author__ = 'Su Lei'

import vtk

# ren = vtk.vtkRenderer()
# renWin = vtk.vtkRenderWindow()
# renWin.AddRenderer(ren)
#
# iren = vtk.vtkRenderWindowInteractor()
# iren.SetRenderWindow(renWin)
#
# line_source = vtk.vtkLineSource()
# line_source.SetPoint1(1, -1, 0)
# line_source.SetPoint2(2, -3, 0)
#
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputConnection(line_source.GetOutputPort())
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
# actor.GetProperty().SetColor(1, 0, 1)
# ren.AddActor(actor)
#
# iren.Initialize()
# renWin.Render()
# iren.Start()

origin = [0.0, 0.0, 0.0]
p0 = [1.0, 0.0, 0.0]
p1 = [0.0, 1.0, 0.0]
p2 = [0.0, 1.0, 2.0]
p3 = [1.0, 2.0, 3.0]

points = vtk.vtkPoints()
points.InsertNextPoint(origin)
points.InsertNextPoint(p0)
points.InsertNextPoint(p1)
points.InsertNextPoint(p2)
points.InsertNextPoint(p3)

lines = vtk.vtkCellArray()
for i in xrange(3):
    line = vtk.vtkLine()
    line.GetPointIds().SetId(0, i)
    line.GetPointIds().SetId(1, i + 1)
    lines.InsertNextCell(line)

linesPolyData = vtk.vtkPolyData()
linesPolyData.SetPoints(points)
linesPolyData.SetLines(lines)

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(linesPolyData)
else:
    mapper.SetInputData(linesPolyData)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetPointSize(5)

ren = vtk.vtkRenderer()
ren.AddActor(actor)
renWin = vtk.vtkRenderWindow()
renWin.SetSize(300, 300)
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

renWin.Render()
iren.Start()

# origin = [0.0, 0.0, 0.0]
# p0 = [1.0, 0.0, 0.0]
# p1 = [0.0, 1.0, 0.0]
#
# pts = vtk.vtkPoints()
# pts.InsertNextPoint(origin)
# pts.InsertNextPoint(p0)
# pts.InsertNextPoint(p1)
#
# red = [255, 0, 0]
# green = [0, 255, 0]
#
# colors = vtk.vtkUnsignedCharArray()
# colors.SetNumberOfComponents(3)
# colors.SetName("Colors")
#
# colors.InsertNextTupleValue(red)
# colors.InsertNextTupleValue(green)
#
# line0 = vtk.vtkLine()
# line0.GetPointIds().SetId(0, 0)
# line0.GetPointIds().SetId(1, 1)
#
# line1 = vtk.vtkLine()
# line1.GetPointIds().SetId(0, 0)
# line1.GetPointIds().SetId(1, 2)
#
# lines = vtk.vtkCellArray()
# lines.InsertNextCell(line0)
# lines.InsertNextCell(line1)
#
# linesPolyData = vtk.vtkPolyData()
# linesPolyData.SetPoints(pts)
# linesPolyData.SetLines(lines)
#
# linesPolyData.GetCellData().SetScalars(colors)
#
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputData(linesPolyData)
#
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
#
# renderer = vtk.vtkRenderer()
# renderWindow = vtk.vtkRenderWindow()
# renderWindow.AddRenderer(renderer)
# renderWindowInteractor = vtk.vtkRenderWindowInteractor()
# renderWindowInteractor.SetRenderWindow(renderWindow)
# renderer.AddActor(actor)
#
# renderWindow.Render()
# renderWindowInteractor.Start()