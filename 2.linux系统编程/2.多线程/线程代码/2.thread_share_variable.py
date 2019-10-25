from threading import Thread
import time

g_num = 100

def work1():
    global g_num
    g_num+=1
    print("修改g_num的值%d"%g_num)

def work2():
    global g_num
    print("查看修改后的g_num值%d"%g_num)

t1 = Thread(target=work1)
t1.start()
time.sleep(1) #延时一秒确保线程1执行完毕
t2 = Thread(target=work2)
t2.start()

#结论：多线程之间共享全局变量