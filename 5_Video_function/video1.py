import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret,frame= cap.read() # erturn treu/false
    if not ret:
        print("frame not found")
        break
    cv2.imshow("video frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()