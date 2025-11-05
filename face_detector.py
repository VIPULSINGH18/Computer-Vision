import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #haarcascade this is an AI brain whose function is used to detect face parts and emotions..

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #we pass gray scale image instead of colorful image because cascade function can work more accurate on gray scale image
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)  #second parameter defines magnifying value, at each iteration our image is getting magnified...


    """"
    detectMultiScale() - scan & detect faces
    1.1 balance, not too slow, blind

    minNeighbors = 5(how much test case we have to pass so that computer can guarantee that right face is detected... if we are passing less number then it is loose checking and if high then it is strong checking )
    """

    for (x,y,w,h) in faces:  #MAY BE WE CAN DETECT MULTIPLE FACES IN ONE FRAME OF VIDEO....
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
    

    """
    x,y - top=left corner

    (x+w, y+h)

    face = [
    (100,150,80,80) face1
    (250,120,90,90) face2
    ]
    x - how far from left
    y - how far from top
    w - width of face
    h - height of face
    """

    cv2.imshow("Webcam Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows() 

# DONE
