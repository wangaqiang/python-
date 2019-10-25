from multiprocessing import Pool
import os
import time

def work():
    print("子进程的id为：%d,父进程的id为%d"%(os.getpid(), os.getppid()))
    for i in range(5):
        print(i)
        # print("子进程做事%d"%i)
        time.sleep(1)
    return "haha"

def work2(xingcan):
    print("做这个事的进程的id为：%d"%os.getpid())
    print("形参的值为：%s"%xingcan)
pool = Pool(3)
pool.apply_async(func=work, callback=work2)

time.sleep(5)
while True:
    time.sleep(1)
    print("主进程的id为：%d"%os.getpid())

# 结论：1.子进程做完事告诉操作系统一声，操作系统让父进程放下手中的活去做callback指定的事,并且操作系统把子进程return的结果当作实参传给callback指定的函数，主进程做完callback中的事后继续做手中的事
# 异步：不等什么时候做不确定
# 同步：等，都是有顺序的