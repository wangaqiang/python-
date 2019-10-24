import time
from multiprocessing import Process
def test():
    while True:
        print("子进程执行的代码")
        time.sleep(1)
p = Process(target = test)  #从multiprocessing模块中导入Process类　　实例化该类便创建一个进程,传入的参数表示该进程要执行的代码
p.start()  #让新进程开始执行test代码

while True:
    print("父进程执行的代码")
    time.sleep(1)

# 阻塞式　　主进程等待子进程执行完才结束