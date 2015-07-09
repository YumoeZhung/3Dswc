__author__ = 'Su Lei'

import vtk

class MouseInteractorStylePP(vtk.vtkInteractorStyleTrackballCamera):
    def __init__(self, parnet=None):
        self.AddObserver('LeftButtonPressEvent', self.leftButtonDown)

    def leftButtonDown(self, *arg):
        pos = self.GetInteractor().GetEventPosition()
        print pos
        r = self.GetInteractor().GetRenderWindow().GetRenderers().GetFirstRenderer()
        self.GetInteractor().GetPicker().Pick(pos[0], pos[1], 0, r)
        picked = self.GetInteractor().GetPicker().GetPickPosition()
        print picked
        self.OnLeftButtonDown()

sphereSource = vtk.vtkSphereSource()
sphereSource.Update()
sphereMapper = vtk.vtkPolyDataMapper()
sphereMapper.SetInputConnection(sphereSource.GetOutputPort())
sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMapper)
ren = vtk.vtkRenderer()
ren.AddActor(sphereActor)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

pointPicker = vtk.vtkWorldPointPicker()
iren.SetPicker(pointPicker)

style = MouseInteractorStylePP()
iren.SetInteractorStyle(style)
ren.SetBackground(1, 1, 1)
renWin.Render()
iren.Initialize()
iren.Start()