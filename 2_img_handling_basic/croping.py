import cv2

img = cv2.imread("img1.png")

if img is not None:
    cropped = img[100:1000,50:1500]
    
    cv2.imshow("cropped img", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()