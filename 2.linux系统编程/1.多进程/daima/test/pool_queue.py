# 进程池之间的通信
from multiprocessing import Manager,Pool
import time
import random


def write(q):
    l = [1,2,3]
    for i in l:
        q.put(i)

def read(q):
    for i in range(q.qsize()):
        print(q.get())
if __name__ == "__main__":
    q = Manager().Queue()
    pool = Pool()
    pool.apply(write, (q,))
    pool.apply(read, (q,))
    pool.close()
    pool.join()
