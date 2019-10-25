# 测试局部变量是否需要加互斥锁
# 试验结果线程中除过全局变量修改时加互斥锁，不修改的情况下可以不加，而且非全局变量不共享，所以也不加
from threading import Thread
import threading
import time

def test():
    g_num = 100
    name = threading.current_thread().name #获取当前线程名字
    if name == "Thread-1":
        g_num +=1
    else:
        time.sleep(1)
    print("%s输出%d"%(name, g_num))

t1 = Thread(target=test)
t1.start()
t2 = Thread(target=test)
t2.start()
