import cv2

img = cv2.imread("img1.png")

if img is not None:
    
    
    pt1 = (100,100)
    pt2 = (400,400)
    color = (255,0,255)
    thickness = 5
    
    #line drawing
    
    # cv2.line(img,pt1,pt2,color,thickness)
    # cv2.imshow("line img", img)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()



    #rectangle drawing
    
    # cv2.rectangle(img,pt2,pt1,color,thickness)
    # cv2.imshow("rectangle img", img)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()
    
    
    
    
    #circle drawing
    
    # cv2.circle(img,(150,150),400,(0,33,44),10)
    # cv2.imshow("circle img", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    #text drawing
    
    cv2.putText(img,"hello Nikgil",(300,300),cv2.FONT_ITALIC,2.3,(0,255,0),5)

    cv2.imshow("text img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
    