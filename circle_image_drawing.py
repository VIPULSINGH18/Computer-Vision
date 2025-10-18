import cv2
image= cv2.imread("py.png")
if image is None:
    print("Image not loaded")
else:
    print("image loaded")

    center= (110,110)
    radius= 93
    color= (0,0,255)
    circle_image= cv2.circle(image,center,radius,color,2)
    cv2.imshow("circle_image",circle_image)
    cv2.imwrite("circle_image.png",circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
