import cv2
import numpy
import os

xx = ['get', 'getBackendName', 'getExceptionMode', 'grab', 'isOpened', 'open', 'read', 'release', 'retrieve', 'set', 'setExceptionMode']
print(dir(cv2.VideoCapture))
print("aaaaaaaaaaaaaaaaaaaaaa")
print(dir(cv2))
cap = cv2.VideoCapture(r'C:\Users\Administrator\Desktop\成都心诚和太科技有限公司\VID_20210911_161835.mp4')
cap = cv2.VideoCapture(0)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #4 ，720
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #3   ，1280
print(frame_height, frame_height)
print("***************************")
frame_height = int(480/frame_width*frame_height) #270
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height) #高
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
data = None
tail_ = r".npy"
save_path = r"I:\导向仪图片"
name1 = "angle_11__updown_dow_23__temperature_20__battery4.8_94x"
name2 = "angle_10__updown_up_0__temperature_16__battery4.8_single_999"
name3 = "angle_10__updown_up_0__temperature_16__battery4.8_single_999"


while cap.isOpened():  # 检查是否成功初始化，否则就使用函数cap.open()
    ret, frame = cap.read()  # ret返回一个布尔值 True/False

    # frame = cv2.flip(frame, flipCode=1)  # 左右翻转,使用笔记本电脑摄像头才有用。
    # flipCode：翻转方向
    # 1：水平翻转；0：垂直翻转；-1：水平垂直翻转

    # Our operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if data is None:
        data = numpy.array([gray])
    else:
        data = numpy.concatenate((data, [gray]), axis=0)
        print(data.shape)
        numpy.save(os.path.join(save_path, name1+tail_), data)
    # Display the resulting frame
    cv2.imshow('frame', gray)
    cv2.setWindowTitle('frame', 'COLOR_BGR2RGB')

    # 如果按下键盘q键，退出摄像头
    key = cv2.waitKey(delay=10)
    if key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




# import numpy
# data = None
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     print(type(gray))
#     if data is None:
#         data = numpy.array([gray])
#     else:
#         data = numpy.concatenate((data, [gray]), axis=0)
#     print(data.shape)
#
#     cv2.imshow('input', gray)
#     if cv2.waitKey(37)==250:
#
#         break
#
# cap.release()
#
# cv2.destroyAllWindows()


