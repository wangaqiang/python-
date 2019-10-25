from threading import Thread

g_num = 0
def task1():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("子线程１g_num的值为：%d"%g_num)

def task2():
    global g_num
    for i in range(1000000):
        g_num+=1
    print("子线程２g_num的值为：%d"%g_num)

t1 = Thread(target=task1)
t1.start()

t2 = Thread(target=task2)
t2.start()
print("主线程g_num的值为：%d"%g_num)

#两个线程各对全局变量g_num加了1000000次　　答案应该是2000000　　但此时结果却不是
# 　因为可能会发生的是在两个线程执行g_num+=1这条语句时相当于两步，第一步是其中一个线程Ａ先算等号右边的,当计算完后将结果准备赋值给g_num时，操作系统让另一个线程Ｂ执行，此时Ａ值还没赋值完成，线程B执行这句话语句时,取原来值，所以造成不是2000000的结果！！！

# 解决办法是进行加锁　　互斥锁的概念引进来