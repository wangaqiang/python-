import os
import time
# os.fork创建一个子进程，主进程返回值大于０，子进程返回值等于0
ret = os.fork()
if ret == 0:
    while True:
        print("----1----")
        time.sleep(1)
else:
    while True:
        print("----2----")
        time.sleep(1)
        