#!/usr/bin/env python

import vtk
import itk
import sys
import argparse


def read_args(*arg):
    """
    read the arguments from argparse and return them.
    """
    input_filename = args.input_filename
    output_filename = args.output_filename

    return input_filename, output_filename
    
def apply_ITK_filter(input_filename,output_filename) :
    """
    Apply a median ITK filter on image.
    Input : input_filename (original image),
            output_filename (name chosen for the filtered image),
    """
    # Read input image
    itk_image = itk.imread(input_filename)

    filtered_image = itk.median_image_filter(itk_image, radius=2)

    #save the result
    itk.imwrite(filtered_image,output_filename)

    return filtered_image

def VTK_rendering(input_filename : str,output_filename : str,filtered_image)->None :
    """
    function to create a render window and display images in it.
    Input:  input_filename (original image),
            output_filename (name chosen for the filtered image),
            filtered_image (image filtered with ITK)
    
    """
    # Try to write vtk images - didn't work
    # writer = vtk.vtkPNGWriter()
    # writer.SetFileName('TestImageO.png')
    # writer.SetInputConnection(vtk_image.GetOutputPort())
    # writer.Write()

    ## Read Images 
    vtk_image = vtk.vtkJPEGReader()
    vtk_image.SetFileName(input_filename)
    vtk_image.Update()

    vtk_filtered = vtk.vtkJPEGReader()
    vtk_filtered.SetFileName(output_filename)
    vtk_filtered.Update()

    # Map the data of the image and connect the output to the input of the mapper.
    OriginalImageMapper = vtk.vtkDataSetMapper()
    OriginalImageMapper.SetInputConnection(vtk_image.GetOutputPort())
    OriginalImageMapper.Update()

    FilteredImageMapper = vtk.vtkDataSetMapper() #there are a lot of vtkMapper : choose wisely
    FilteredImageMapper.SetInputConnection(vtk_filtered.GetOutputPort())
    FilteredImageMapper.Update()
    
    # Create an actor to represent the original Image
    actor = vtk.vtkActor()
    actor.SetMapper(OriginalImageMapper)
  
    actor2 = vtk.vtkActor()
    actor2.SetMapper(FilteredImageMapper)
    
    # Create 2 Renderers and assign actors to them.
    # Setting the view of the actors in the window.
    ren = vtk.vtkRenderer()
    ren.AddActor(actor)
    ren.SetViewport(0.0, 0.0, 0.5, 1.0)

    ren2 = vtk.vtkRenderer()
    ren2.AddActor(actor2)
    ren2.SetViewport(0.5, 0.0, 1.0, 1.0)

    # Create the render window. add the 2 renderers.
    # Set the size and name of the window.
    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.AddRenderer(ren2)
    renWin.SetSize(800,600)
    renWin.SetWindowName('1st Exercise')
   
    iren = vtk.vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    iren.Initialize()
    iren.Start() #don't forget to start :)


if __name__ == '__main__' :

    parser = argparse.ArgumentParser(description="Read a  image, apply an ITK filter and display both image,original and filtered,in a VTK renderer")
    
    parser.add_argument("input_filename", type=str, help="File name of the picture in input")
    parser.add_argument("output_filename", type=str, help="File name of the filtered image")
    args = parser.parse_args()
   
    input, output = read_args(args)
    filteredITK_image = apply_ITK_filter(input,output)
    VTK_rendering(input,output,filteredITK_image)