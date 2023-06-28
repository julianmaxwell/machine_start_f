import cv2
import testk
import socket

from multiprocessing import Pipe

def get_machine_rule_test():
    send_out_from_video, recv_from_video = Pipe()
    testk.test_all_gaze(pipout=send_out_from_video)


def show_2():
    mm0 = cv2.VideoCapture(0)
    mm1 = cv2.VideoCapture(1)
    while True:
        xx0 = mm0.read()[1]
        xx1 = mm1.read()[1]
        cv2.imshow("xx0", xx0)
        cv2.imshow("xx1", xx1)
        cv2.waitKey(30)


    # cv2.resize(xx, (480, 640))

def show_3():
    mm0 = cv2.VideoCapture(0)
    mm1 = cv2.VideoCapture(1)
    mm2 = cv2.VideoCapture(2)
    while True:
        xx0 = mm0.read()[1]
        xx1 = mm1.read()[1]
        xx2 = mm2.read()[1]
        print("***************************")
        if xx0 is not None:
            print(xx0.shape)
            cv2.imshow("xx0", xx0)
        if xx1 is not None:
            print(xx1.shape)
            cv2.imshow("xx1", xx1)
        if xx2 is not None:
            print(xx2.shape)
            cv2.imshow("xx2", xx2)
        cv2.waitKey(30)

# show_2()
show_3()