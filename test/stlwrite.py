__author__ = 'Su Lei'

import vtk

filename = 'test.stl'
sphereSource = vtk.vtkSphereSource()
sphereSource.Update()

stlWriter = vtk.vtkSTLWriter()
stlWriter.SetFileName(filename)
stlWriter.SetInputConnection(sphereSource.GetOutputPort())
stlWriter.Write()

reader = vtk.vtkSTLReader()
reader.SetFileName(filename)
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
ren.AddActor(actor)
iren.Initialize()
renWin.Render()
iren.Start()
