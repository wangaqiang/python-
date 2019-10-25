from threading import Thread, Lock
import time

class Work1(Thread):
    def run(self):
        while True:
            if mutex1.acquire():
                print("task1")
                time.sleep(1)
                mutex2.release()

class Work2(Thread):
    def run(self):
        while True:
            if mutex2.acquire():
                print("task2")
                time.sleep(1)
                mutex3.release()

class Work3(Thread):
    def run(self):
        while True:
            if mutex3.acquire():
                print("task3")
                time.sleep(1)
                mutex1.release()

mutex1 = Lock()
mutex2 = Lock()
mutex3 = Lock()
mutex2.acquire()
mutex3.acquire()

if __name__ == "__main__":
    t1 = Work1()
    t2 = Work2()
    t3 = Work3()
    t1.start()
    t2.start()
    t3.start()
