# 导入mulitprocessing中的Queue
from multiprocessing import Process,Queue
import time
import random

def write(q):
    l = [1,2,3]
    for i in l:
        a = q.put(i)
        
def read(q):
    while True:
        if not q.empty():
            a = q.get()
            print(a)
        else:
            break
            
if __name__ == "__main__":
    q = Queue()
    process_write = Process(target=write, args=(q,))
    process_write.start()
    process_write.join()
    process_read = Process(target=read, args=(q,))
    process_read.start()