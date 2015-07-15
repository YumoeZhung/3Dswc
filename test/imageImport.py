__author__ = 'Su Lei'

import vtk
import numpy as np
import cv2 as cv

test_image = cv.imread('1.tif', cv.CV_LOAD_IMAGE_UNCHANGED)
print test_image.shape, test_image.dtype
# test_image.reshape((1, 92 * 173))

imageImport = vtk.vtkImageImport()
imageImport.SetDataSpacing(1, 1, 1)
imageImport.SetDataOrigin(0, 0, 0)
imageImport.SetDataExtent(0, 172, 0, 91, 0, 0)
imageImport.SetWholeExtent(0, 172, 0, 91, 0, 0)
imageImport.SetDataScalarTypeToUnsignedChar()
imageImport.SetNumberOfScalarComponents(1)
# imageImport.CopyImportVoidPointer(test_image.tostring(), len(test_image.tostring()))
# imageImport.SetImportVoidPointer(test_image)
# imageImport.CopyImportVoidPointer(test_image, test_image.size)
imageImport.Update()

actor = vtk.vtkImageActor()
actor.SetInputData(imageImport.GetOutput())

ren = vtk.vtkRenderer()
ren.AddActor(actor)
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
style = vtk.vtkInteractorStyleImage()
iren.SetInteractorStyle(style)
renWin.SetSize(500, 500)
iren.Initialize()
iren.Start()

