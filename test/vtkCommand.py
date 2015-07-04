__author__ = 'Su Lei'

import vtk

class VtkMyCallback(vtk.vtkCommand):
    def __init__(self):
        pass

cone = vtk.vtkConeSource()
cone.SetHeight(3.0)
cone.SetRadius(1.0)
cone.SetResolution(10)

coneMapper = vtk.vtkPolyDataMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())

coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

ren1 = vtk.vtkRenderer()
ren1.AddActor(coneActor)
ren1.SetBackground(0.1, 0.2, 0.4)
ren1.ResetCamera()

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(300, 300)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
interactor.SetRenderWindow(renWin)

def DummyFunc1(obj, ev):
    print obj.GetActiveCamera().GetPosition()

def DummyFunc2(obj, ev):
    print 'ggggg'

# interactor.RemoveObservers('LeftButtonPressEvent')
# interactor.AddObserver('LeftButtonPressEvent', DummyFunc1, 1.0)
# interactor.AddObserver('LeftButtonPressEvent', DummyFunc2, -1.0)
# interactor.Initialize()
# interactor.Start()

ren1.AddObserver(vtk.vtkCommand.StartEvent, DummyFunc1)

for i in xrange(360):
    renWin.Render()
    ren1.GetActiveCamera().Azimuth(1)
