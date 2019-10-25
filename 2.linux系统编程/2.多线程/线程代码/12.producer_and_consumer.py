from threading import Thread
from queue import Queue
import time

class Producer(Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg =self.name+"生成产品"+str(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + q.get()
                    print(msg)
            time.sleep(1)
if __name__ == "__main__":
    q = Queue()
    for i in range(500):
        q.put("存入原始产品"+str(i))

    for i in range(2):
        p = Producer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()
