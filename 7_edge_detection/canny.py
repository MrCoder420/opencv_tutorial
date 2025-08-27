import cv2

img = cv2.imread("img1.jpg",cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,50,10)

cv2.imshow("original img", img)
cv2.imshow("canny edge detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()