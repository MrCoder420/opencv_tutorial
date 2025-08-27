import cv2


face_cascade = cv2.CascadeClassifier("8_face_detection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("8_face_detection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("8_face_detection/haarcascade_smile.xml")

cap= cv2.VideoCapture(0)

while True:
    
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    eye = eye_cascade.detectMultiScale(gray,1.1,10)
    smile = smile_cascade.detectMultiScale(gray,1.7,22)
    
    for (x,y,w,h) in faces :
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       
    
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    
    if len(eye) >0:
        cv2.putText(frame,"eye detected",(x,y-50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        
    if(len(smile))>0:
        
        cv2.putText(frame,"smile detected",(x,y-80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.imshow("Face, Eye and Smile Detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    