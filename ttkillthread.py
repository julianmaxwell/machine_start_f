import cv2
import numpy
mm = cv2.VideoCapture(r"D:\钻杆操作台照片\IMG_20190518_082807.jpg")

xx = mm.read()[1]
print(xx.shape)
xx = cv2.resize(xx, (400, 680))

xx = cv2.Canny(xx, 80, 180, 3)
xx = cv2.GaussianBlur(xx, (5, 5), 0)
xx = numpy.expand_dims(xx, axis=2)
print(xx.shape)
cv2.imshow("test", xx)
cv2.waitKey()