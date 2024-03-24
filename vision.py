import pytesseract
import cv2

# Here the image get read
img = cv2.imread('image1.jpg')
img = cv2.resize(img, (600,360))

#Here the image content will convert into string then display
print(pytesseract.image_to_string(img))

cv2.imshow('result', img)
cv2.waitkey(0)