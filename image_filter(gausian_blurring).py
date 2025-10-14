import cv2
image= cv2.imread("free-nature-images.jpg")
blurred= cv2.GaussianBlur(image,(7,7),0) #third parameter here is standard deviation of x and y. if we use 0 then default value will be used for our output image..

cv2.imshow("normal image",image)
cv2.imshow("blur_image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
