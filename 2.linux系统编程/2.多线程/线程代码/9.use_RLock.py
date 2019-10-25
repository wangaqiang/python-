# 一个锁也可以出现死锁问题 因为已经锁上　还没打开接着去锁就会产生死锁
from threading import Thread,Lock
def work():
    if lock.acquire():
        print("上锁成功，接下来再进行上锁，会出现死锁现象．．．")
        lock.acquire()
        lock.release()
        lock.release()
        print("解锁成功，可惜在这出现不了．．．")

lock = Lock()
if __name__ == "__main__": 
    t1 = Thread(target=work)
    t1.start()