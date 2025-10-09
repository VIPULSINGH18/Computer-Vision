import cv2
image= cv2.imread("py.png")
if image is not None:
    h,w,c= image.shape
    print("Image Loaded")
    print("Height:",h)
    print("Width:",w)
    print("Channels:",c) #it is going to color channel of our loaded image's pixel...
else:
    print("Could not load image")
