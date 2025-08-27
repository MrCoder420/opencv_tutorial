import cv2

img = cv2.imread("img1.png")

if img is None:
    print("Image not found")
    exit()
else:
    print("img loaded   ")
    
    rs= cv2.resize(img,(1024,1024))
    
    cv2.imshow("resized img",rs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite("resize_img.png",rs)
    