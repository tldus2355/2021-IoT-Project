import cv2
img = cv2.imread('image.jpg')
img2 = cv2.resize(img, (1000, 800))
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# EDGE선 추출
edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

# cv2.imshow('image', img)
# cv2.imshow('image2', img2)
# cv2.imshow('GRAY', img3)

cv2.imshow('image1', edge1)
cv2.imshow('image2', edge2)
cv2.imshow('image3', edge3)

# enter : 13, esc : 27
while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('image_GRAY.jpg', img3)

cv2.destroyAllWindows()