from threading import Thread,Lock

g_num = 0
def task1():
    global g_num
    for i in range(100000):
        mutax.acquire() #与另一个子线程抢着上锁　加锁加在越少的地方越好
        g_num+=1
        mutax.release() #成功上锁后解锁
    print("子线程1的结果为%d"%g_num)


def task2():
    global g_num
    for i in range(100000):
        mutax.acquire()  #返回的是bool值
        g_num+=1
        mutax.release()
    print("子线程2的结果为%d"%g_num)

# 创建一把互斥锁
mutax = Lock()

t1 = Thread(target=task1)
t1.start()
t2 = Thread(target=task2)
t2.start()
print("主线程的结果为%d"%g_num)

# 结论：当多个线程同时修共享的数据时，需要进行同步控制．
# 同步的意思是协同步调，指协同，协作．
# 此时引进互斥锁，原理是阻止了线程并发运行，存在问题是出现死锁．