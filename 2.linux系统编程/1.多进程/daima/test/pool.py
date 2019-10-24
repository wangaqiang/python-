from multiprocessing import Pool
import os
import time
def test(num):
    for i in range(3):
        print("pid=%d======%d="%(os.getpid(), num))
        time.sleep(1)

if __name__=="__main__":
    pool = Pool(3) #创建进程池  3代表最多有三个进程

    # 向进程池添加任务
    for i in range(5):
        print("add task%d"%i)
        pool.apply_async(test, (i,)) #test为进程要执行的任务 元祖代表要传入的参数

    # 关闭进程池，作用是因为进程池刚创建时默认为开启状态(即可以为进程池添加任务)，调用该方法后关闭进程池(即不能在添加任务进去)
    pool.close()

    # 主进程要等进程里的进程完成任务后才能结束战斗
    pool.join()
