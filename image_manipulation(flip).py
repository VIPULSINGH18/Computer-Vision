import cv2
image= cv2.imread("py.png")
if image is None:
    print("Image is not loaded")
else:
    print("Image is loaded sucessfully")
    flip_horizontal= cv2.flip(image,1)
    flip_vertical= cv2.flip(image,0)
    flip_both= cv2.flip(image,-1)
    cv2.imshow("original image",image)
    cv2.imshow("horizontal_Image",flip_horizontal)
    cv2.imshow("vertical_image",flip_vertical)
    cv2.imshow("flip_both",flip_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
