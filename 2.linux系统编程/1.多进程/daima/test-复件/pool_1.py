from multiprocessing import Pool
import os
import time

def tt(num):
    for i in range(3):
        print("pid=%d======%d="%(os.getpid(), num))
        time.sleep(1)

if __name__ =="__main__": #为什么要把实例化进程池放进这句话中
    pool = Pool(3) #创建进程池  3代表最多有三个进程


for i in range(5):
    print("add task%d"%i)
    pool.apply_async(tt, (i,)) #test为进程要执行的任务 元祖代表要传入的参数

#pool.close()
pool.join() #必须在close()或者terminate()方法后调用
