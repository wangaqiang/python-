import time

from threading import Thread

def test():
    print("hello world")
    time.sleep(1)

for i in range(5):
    t = Thread(target=test)
    t.start()