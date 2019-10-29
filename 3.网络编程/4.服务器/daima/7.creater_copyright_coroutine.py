import time

def a():
    while True:
        print("_____________a_____________")
        yield
        time.sleep(1)

def b(a):
    while True:
        print("_____________b_____________")
        a.__next__()
        time.sleep(1)

if __name__ == "__main__":
    c = a()
    b(c)