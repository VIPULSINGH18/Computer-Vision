import cv2
image= cv2.imread("py.png")
if image is None:
    print("image not laodaed")
else:
    print("image  loaded")

    resize_image= cv2.resize(image,(100,100))
    cv2.imwrite("resize_py.png",resize_image)
    cv2.imshow("resize_image",resize_image)
    cv2.imshow("normal_image",image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

