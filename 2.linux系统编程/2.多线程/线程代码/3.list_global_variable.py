from threading import Thread
import time

def work1(g_list):
    g_list.append(4)  #在这个线程里对传进来的列表进行修改
    print(g_list)  

def work2(g_list):
    time.sleep(1)  #这个线程延时一秒确保上面的线程执行完毕
    print(g_list)  #在这个线程里获取传进来的列表值看是否发生了改变


g_list = [1,2,3]
th1 = Thread(target=work1, args=(g_list,))
th1.start()
th2 = Thread(target=work2, args=(g_list,))
th2.start()

#结论：在一个进程中多个线程共享全局变量