import cv2
image= cv2.imread("py.png")
if image is None:
    print("Image not loaded")
else:
    print("image loaded")
    #syntax: cv2.putText(image_source, text,origin_of_text, text_style,text_size,color,thickness)
    text_image= cv2.putText(image,"Python programmers",(11,215), cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,200,0),2)
    cv2.imshow("text_image",text_image)
    cv2.imwrite("text_image.png",text_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()