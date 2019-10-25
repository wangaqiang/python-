import threading

t_local = threading.local()

def work2():
    std = t_local.student
    print("hello %s in (%s)"%(std, threading.current_thread().name))

def work1(canshu1):
    t_local.student = canshu1
    work2()

t1 = threading.Thread(target=work1, args=("laowang",), name="xiancheng1")
t1.start()

t2 = threading.Thread(target=work1, args=("qiangge",), name="xiancheng2")
t2.start()