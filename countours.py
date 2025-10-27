import cv2

img = cv2.imread("shape.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

#to find and collect contours we will first convert our image into grey scale and then will do threshholding...

#FIND CONTOURS
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

#syntax: (img_source, contours list, parameter, color , thickness)... parameter will tell of how many shape we have to make boundary, as an image can contain multiple shapes.. if we will use -1 then every shape get traced....
cv2.drawContours(img, contours, -1, (0,255,0), 3)  #trace the boundary and edges of our shape using collected contours....



cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()