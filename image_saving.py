import cv2
image= cv2.imread("py.png")
if image is not None:
    success= cv2.imwrite("output_python.png",image)
    if success:
        print("Image saved successfully")
    else:
        print("Image not saved")
else:
    print("Image is not loaded properly")