"""

* img1 img2 height width same
** use only black and white
*** 

"""
import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8") #created array of 300 cols and 300 rows with 0 value of pixel
img2 = np.zeros((300,300), dtype="uint8") #created array of 300 cols and 300 rows with 0 value of pixel

cv2.circle(img1, (150, 150), 100, 255, -1) #(img_src,center,radius,color,thickness)

cv2.rectangle(img2, (100,100), (250,250), 255, -1) #(img_src,two points,color,thickness)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2) #combines the two image
bitwise_not = cv2.bitwise_not(img1) #interchange the color value

cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)
cv2.imshow("AND", bitwise_and)
cv2.imshow("OR", bitwise_or)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()