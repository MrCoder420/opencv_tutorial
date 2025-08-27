import cv2

img = cv2.imread("img1.png")

if img is not None:
    
    h,w,c = img.shape
    
    # center_p= (w//2,h//2)
    
    # m = cv2.getRotationMatrix2D(center_p,180,0.6)
    
    # ro = cv2.warpAffine(img,m,(w,h))
    
    # cv2.imshow("rotated img", ro)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()
    
    f =cv2.flip(img,1) # 0- vertical, 1-horizontal, -1-both
    
    
    cv2.imshow("flip img", f)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()