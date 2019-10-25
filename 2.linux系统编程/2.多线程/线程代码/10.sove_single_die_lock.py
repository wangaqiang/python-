#　解决一个锁子产生的死锁问题　threading模块中有RLock，其相比Lock多了一个count变量，该变量用来记录上锁次数

import time
from threading import Thread, RLock

class Mythread(Thread):
    def run(self):
        if lock.acquire():
            print("线程%s上锁成功..."%self.name)
            time.sleep(1)
            lock.acquire()
            lock.release()
            print("线程%s解锁成功..."%self.name)
            lock.release()

if __name__ == "__main__":
    print("主线程开始")
    lock = RLock()
    t1 = Mythread()
    t2 = Mythread()
    t1.start()
    t2.start()
    print("主线程结束")

