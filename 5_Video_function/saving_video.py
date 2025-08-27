import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec =cv2.VideoWriter_fourcc(*'XVID')

rec = cv2.VideoWriter("output.avi", codec, 20, (frame_width, frame_height))

while True:
    
    ret,frame = camera.read()
    rec .write(frame)
    cv2.imshow("video frame", frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
camera.release()
cv2.destroyAllWindows()
    
    
    