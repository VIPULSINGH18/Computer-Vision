import cv2
image= cv2.imread("py.png")
if image is not None:
    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale image",gray) #black and white image
    cv2.imwrite("black_py.png",gray)
    cv2.imshow("RGB_image",image) #rgb image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:

    print("Image not loaded") //hlo
