from multiprocessing import Process, Lock
import time
xx = Lock()
xx.acquire()
xx.release()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def testn(n, ):
    global xx

    # print(n)
    # print(data[n])
    # print(id(xx))
    # xx.acquire()
    xx.acquire()
    print(data)
    print(data[n])
    time.sleep(3)
    print("xxxxxxxxxxxxxxxxxxxxxxxx")
    xx.release()

if __name__ == '__main__':
    for i in range(1, 5):
        t1 = Process(target=testn, args=(i, ))
        t1.start()
