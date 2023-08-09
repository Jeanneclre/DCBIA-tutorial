#!/usr/bin/env python3

import itk
import numpy as np
import sys
import cv2
import os

# input_filename = sys.argv[1]
# output_filename = sys.argv[2]

# # Read input image
# itk_image = itk.imread(input_filename)

# # Run filters on itk.Image

# # View only of itk.Image, pixel data is not copied
# array_view = itk.array_view_from_image(itk_image)

# # Copy of itk.Image, pixel data is copied
# array_copy = itk.array_from_image(itk_image)
# # Equivalent
# array_copy = np.asarray(itk_image)

# # Image metadata
# # Sequences, e.g. spacing, are in zyx (NumPy) indexing order
# metadata = dict(itk_image)

# # Pixel array and image metadata together
# # in standard Python data types + NumPy array
# # Sequences, e.g. spacing, are in xyz (ITK) indexing order
# image_dict = itk.dict_from_image(itk_image)


# median = itk.median_image_filter(array_copy, radius=2)


# # Convert back to ITK, view only, data is not copied
# itk_image_view = itk.image_view_from_array(median)

# # Convert back to ITK, data is copied
# itk_image_copy = itk.image_from_array(median)

# # Add the metadata
# for k, v in metadata.items():
#     itk_image_view[k] = v

# # Save result
# itk.imwrite(itk_image_view, output_filename)

# # Convert back to itk image data structure
# itk_image = itk.image_from_dict(image_dict)

### FOR COLORFUL PICTURES ###
###                       ###
input_filename = sys.argv[1]
thresh_filemane = sys.argv[2]
output_filename = sys.argv[3]

img = cv2.imread(input_filename)
grimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(grimg,90,255,cv2.THRESH_BINARY_INV)

cv2.imwrite(thresh_filemane,thresh)

image = itk.imread(thresh_filemane)

median = itk.median_image_filter(image, radius=2)

itk.imwrite(median, output_filename)

os.remove(thresh_filemane)