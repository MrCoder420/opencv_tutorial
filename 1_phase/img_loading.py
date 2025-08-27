import cv2 as cv


img = cv.imread("phase_1/img1.png",1)

if img is None:
    print("Image not found")
    exit()
else:
    # print("Image loaded successfully")
    # cv.imshow("Image",img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    
    # print("img saving")
    # cv.imwrite("img_copy.png",img)
    
    # #  img dimensions
    
    # h,w,c = img.shape
    # print("Height:",h)
    # print("Width:",w)
    # print("Channels:",c)

    # img grayscale conversion
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Image",gray)
    cv.waitKey(0)
    cv.destroyAllWindows()
