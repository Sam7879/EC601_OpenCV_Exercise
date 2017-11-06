import cv2

img = cv2.imread('baboon.jpg')

cv2.imshow("Original Image", img)

[b,g,r] = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Red', r)
cv2.imshow('Green', g)
cv2.imwrite('Blue.png', b)
cv2.imwrite('Red.png', r)
cv2.imwrite('Green.png', g)
RGB_part = img[20,25]
print("RGB part",RGB_part)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
[h,s,v] = cv2.split(hsv)
cv2.imshow('Hue', h)
cv2.imshow('Saturation', s)
cv2.imshow('Value', v)
cv2.imwrite('Hue.png', h)
cv2.imwrite('Saturation.png', s)
cv2.imwrite('Value.png', v)
hsv_part = hsv[20, 25]
print("HSV part", hsv_part)

YCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
[y,Cb,Cr] = cv2.split(YCC)
cv2.imshow('Y', y)
cv2.imshow('Cb', Cb)
cv2.imshow('Cr', Cr)
cv2.imwrite('Y.png', y)
cv2.imwrite('Cb.png', Cb)
cv2.imwrite('Cr.png', Cr)
YCC_part = YCC[20, 25]
print("YCC part:", YCC_part)

cv2.waitKey(0)