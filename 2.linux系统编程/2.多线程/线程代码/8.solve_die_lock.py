# 死锁解决办法：给Lock().acquire()传参数，则timeout!=-1，则等待这么长时间后就不再等待了
from threading import Thread, Lock

def work1():
    if mutex1.acquire():
        print("1锁上锁")
        if mutex2.acquire(timeout=2):  #添加了时间参数,不再发生死锁　等这个时间后，不等了
            mutex2.release()
        mutex1.release()
def work2():
    if mutex2.acquire():
        print("2锁上锁")
        if mutex1.acquire():
            mutex1.release()
        mutex2.release()

mutex1 = Lock()
mutex2 = Lock()

t1 = Thread(target=work1)
t2 = Thread(target=work2)
t1.start()
t2.start()