import cv2
image= cv2.imread("py.png")
if image is None:
    print("Image not loaded")
else:
    print("image loaded")
    pt_1= (20,20)
    pt_2= (200,200)
    color=(0,0,255)

    rectangle_on_image= cv2.rectangle(image,pt_1,pt_2,color,2)
    cv2.imwrite("rectangle_image.png",rectangle_on_image)
    cv2.imshow("rectangle_image",rectangle_on_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
