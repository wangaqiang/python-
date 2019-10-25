from threading import Thread,Lock

def work1():
    if mutex_1.acquire():  #尝试锁第一把锁子
        print("锁一已上锁")
        if mutex_2.acquire(): #尝试锁第二把锁子如果这把锁子能锁上即另一个线程还没对这把锁子锁上　则程序没异常，否则程序产生死锁
            mutex_2.release()
        mutex_1.release()

def work2():
    if mutex_2.acquire(): #对锁二进行上锁
        print("锁二进行上锁")
        if mutex_1.acquire(): 
            mutex_1.release()
        mutex_2.release()

mutex_1 = Lock()
mutex_2 = Lock()
t1 = Thread(target=work1)
t2 = Thread(target=work2)

t1.start()
t2.start()

#　可能你等我解锁后，才能上锁，我在等你解锁才能解锁　　然后就死锁了