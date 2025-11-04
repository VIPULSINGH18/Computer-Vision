import cv2
camera= cv2.VideoCapture(0)
frame_width= int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height= int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec= cv2.VideoWriter_fourcc(*'XVID')
recorder=cv2.VideoWriter("my_video.avi",codec,30,(frame_width,frame_height))

while True:
    ret,frame= camera.read()
    if ret==False:
        break
    
    recorder.write(frame)  #records each and every frame until our webcam stops
    cv2.imshow("recording_feed",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("quit...")
        break

camera.release()  #stop capturing video function
recorder.release() #stop recording video function
cv2.destroyAllWindows()
