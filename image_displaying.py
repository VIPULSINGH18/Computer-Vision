#displaying image...
import cv2  #importing open cv library
image= cv2.imread("py.png")  #reading image file
if image is not None:
  cv2.imshow("Image showing",image) #open the window
  cv2.waitKey(0)  #wait for a key
  cv2.destroyAllWindows() #close the window
else:
  print("Could not load the image")
