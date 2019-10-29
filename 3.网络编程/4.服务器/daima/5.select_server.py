import select
from socket import *

# 创建套接字
serversocket = socket(AF_INET, SOCK_STREAM)

# 绑定
serversocket.bind(("", 7777))

# 监听
serversocket.listen(6)

inputs = [serversocket]

while True:
    readable, writeable, exceptional = select.select(inputs, [], []) 
    # select默认是堵塞的,检测到满足条件解堵塞.有三个参数
        # 检测第一个列表里的套接字能不能收数据
        # 检测第二个列表中的套接字能不能发数据
        # 检测第三个列表中的套解字是否产生了异常 

    for sock in readable: # 检测到有可以读的套接字
        if sock == serversocket: # 判断是有新的客户端链接的情况下
            clientsocket, clientinfo = sock.accept()
            inputs.append(clientsocket) # 将新链接的客户端存放在inputs列表中

        else: # 有客户端收到消息的情况下
            recvdata = sock.recv(1024)
            if recvdata:
                sock.send(recvdata)
            else:
                inputs.remove(sock)
                sock.close()
serversocket.close()