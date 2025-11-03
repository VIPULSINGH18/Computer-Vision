import cv2
cap= cv2.VideoCapture(0) #0 tells our computer to use their own web cam and 1 is used if we have to access another device's webcam...

while True:
    ret,frame= cap.read() #it will return true value if webcam is working properly and return single frame of video..

    if ret==False:
        print("could not read frame")
        break

    cv2.imshow("webcam Feed",frame) #display frame on our screen...

    if cv2.waitKey(1) & 0xFF==ord('q'):  #our system wait for 1 ms and check whether user has clicked on q button or not, if not then loop will continue running...
        print("quitting...")
        break

cap.release()
cv2.destroyAllWindows()

