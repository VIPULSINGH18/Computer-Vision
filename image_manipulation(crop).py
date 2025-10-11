import cv2
image= cv2.imread("py.png")
if image is not None:
    crop= image[20:200,20:200]
    cv2.imshow("normal_image",image)
    cv2.imwrite("crop_py.png",crop)
    cv2.imshow("cropped_image",crop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")