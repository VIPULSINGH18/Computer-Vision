import cv2
import numpy as np

image = cv2.imread("low_r.png")

sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(image, -1, sharpen_kernel) #second parameter is depth of the image,-1 signify that depth of output image will be same as imput image...
                                                    # now depth detrmines the data types of each and every pixel...
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()