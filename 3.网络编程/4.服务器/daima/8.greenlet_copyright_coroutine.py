import time
from greenlet import greenlet

def test1():
    while True:
        print("____________a-------------------")
        gr2.switch()
        time.sleep(1)

def test2():
    while True:
        print("____________b-------------------")
        gr1.switch()
        time.sleep(1)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()