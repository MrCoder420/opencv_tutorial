import cv2 as cv2

print("enter location of img")
input_location = input()
img = cv2.imread(input_location,1)

if img is None:
    print("Image not found")
    exit()
else:
    
    gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    
    print("1.img showing")
    print("2.img saving")
    c = int(input())
    if c==1:

        cv2.imshow("gray img",gray_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imwrite("gray_img.png",gray_img)
