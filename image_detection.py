import cv2

img = cv2.imread("flower.png")
grey_image= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #we convert the image into gray scale because we apply canny detection and threshold function only on numeric value between 0 to 255

edges = cv2.Canny(grey_image, 50, 150) #we pass two paramter t1 and t2... value less than t1 becomes 0 (black) and value above the t2 becomes 255(white)

cv2.imshow("Original Image", img)
cv2.imshow("grey_image",grey_image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()