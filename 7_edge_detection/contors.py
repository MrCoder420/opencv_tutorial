import cv2

img = cv2.imread("triangle.jpg")
if img is None:
    print("Error: Could not load image")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

print(f"Found {len(contours)} contours")

for i, contour in enumerate(contours):
    # Filter out small contours (noise)
    area = cv2.contourArea(contour)
    if area < 100:  # Skip small contours
        continue
    
    print(f"Contour {i}: Area = {area}")
    approx = cv2.approxPolyDP(contour, 0.02*cv2.arcLength(contour, True), True)
    corners = len(approx)
    print(f"Shape has {corners} corners")

    if corners == 3:
        shape = "triangle"
    elif corners == 4:
        shape = "rectangle/square"
    elif corners == 5:
        shape = "pentagon"
    elif corners == 6:
        shape = "hexagon"
    elif corners == 10:
        shape = "star"
    else:
        shape = "circle"
    
    print(f"Detected: {shape}")
    
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Show both original threshold and final result
cv2.imshow("Threshold", thresh)
cv2.imshow("Shape Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()