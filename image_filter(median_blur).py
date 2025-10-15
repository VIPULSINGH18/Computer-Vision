import cv2
image= cv2.imread("noisy_f.png")
blur= cv2.medianBlur(image,5) #kernel size should always be possitive to have one unique center pixel inside the kernel

cv2.imshow("normal_image",image)
cv2.imshow("blur_image",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()


# notes: gaussian blur is used to blur or smooth the image whereas median blur is used to remove noise and random small black and white points from the image
#        gaussian blur uses average of all pixel points inside the kernel whereas median blur sort all the pixel points inside the kernel and take center value as a result(away from noise and less fluctuated)
