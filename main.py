import cv2

img = cv2.imread('test.jpg')

print(img.shape)
img = cv2.resize(img,(1500, 500))
print(img.shape)
print(img)

cv2.imshow('Result', img)
cv2.waitKey(0)


