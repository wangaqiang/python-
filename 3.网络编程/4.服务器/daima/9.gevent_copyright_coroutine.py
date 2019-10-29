import gevent

def test(n):
    for i in range(n):
        print(i)
        gevent.sleep(1)
g1 = gevent.spawn(test, 5)
g2 = gevent.spawn(test, 5)
g3 = gevent.spawn(test, 5)

g1.join()
g2.join()
g3.join()