import cv2
image= cv2.imread("py.png")
if image is None:
    print("image not loaded")
else:
    print("Image loaded")

    (h,w)= image.shape[:2]
    center= (w//2,h//2)
    M= cv2.getRotationMatrix2D(center,-90,1.0)  #to rotate clockwise we have to use negative sign and for anti clockwise we have to use positive sign...
    rotated= cv2.warpAffine(image,M,(w,h))

    cv2.imshow("normal image",image)
    cv2.imshow("rotated_image",rotated)
    cv2.imwrite("rotated.png",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()