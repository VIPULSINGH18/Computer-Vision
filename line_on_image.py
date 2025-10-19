import cv2
image= cv2.imread("py.png")
if image is None:
    print("Image not loaded")
else:
    print("image loaded")
    pt_1= (30,200)
    pt_2= (200,200)
    color= (0,0,255)

    line_image=cv2.line(image,pt_1,pt_2,color,2)
    cv2.imshow("image_on_line",line_image)
    cv2.imwrite("line_image.png",line_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
