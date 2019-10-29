import select
from socket import *

# 1创建套接字
serversocket = socket(AF_INET, SOCK_STREAM)

# 2绑定
serversocket.bind(("", 8888))

# 3设置为被动套接字
serversocket.listen(5)

# 4创建epoll对象
epoll = select.epoll()

# 5注册套接字的文件描述符
epoll.register(serversocket.fileno(), select.EPOLLIN|select.EPOLLET)

# 根据套接字的文件描述符存放套接字的字典
connections = {}
addresses = {}

while True:
    epoll_list = epoll.poll() #　进行监听，默认堵塞

    for fd, events in epoll_list:
        if fd == serversocket.fileno(): # 如果监听到的套接字的文件描述符与主动套接字的监听描述符相等

            clientsocket, clientinfo = serversocket.accept()

            # 将客户端套接字的信息进行保存
            connections[clientsocket.fileno()] = clientsocket
            addresses[clientsocket.fileno()] = clientinfo

            # 将新得到的文件描述符注册进对象
            epoll.register(clientsocket.fileno(), select.EPOLLIN|select.EPOLLET)

        elif events == select.EPOLLIN: # 判断事件是否是可以收消息的事件
            recvdata = connections[fd].recv(1024)

            if len(recvdata) > 0:
                print("recv:%s"%recvdata)
            else:
                # 没收到数据时从注册中删除文件描述符
                epoll.unregister(fd)
                connections[fd].close()
serversocket.close()