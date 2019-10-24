#使用Process类的子类创建子进程　　主进程优先于子进程
import time
from multiprocessing import Process

class MyProcess(Process):
    def run(self):
        for i in range(5):
            print(i)

if __name__ =="__main__":
    myprocess = MyProcess() #通过Process类的子类的对象创建进程
    myprocess.start()  #启动进程
    print("main")
