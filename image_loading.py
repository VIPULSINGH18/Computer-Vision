#loading image

import cv2  #importing open cv library
image= cv2.imread("py.png")  #reading image file
if image is None:
  print("Error: Image not found")
else:
  print("Image loaded successfully")
