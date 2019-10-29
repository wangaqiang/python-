from socket import *

# 1创建套接字
serversocket = socket(AF_INET, SOCK_STREAM)

# 2绑定
serversocket.bind(("", 6777))
serversocket.setblocking(False)

# 3设置为被动套接字
serversocket.listen(5)

# 存放客户端信息的列表
clientlist = []
while True:
    # 4等待链接
    try:
        clientsocket, clientinfo = serversocket.accept() # 会产生异常
    except:
        pass
    else:
        print("来了一个新客户%s"%str(clientinfo))
        clientsocket.setblocking(False)
        clientlist.append((clientsocket, clientinfo))

    for clientsocket, clientinfo in clientlist:
        try:
            recvdata = clientsocket.recv(1024) # 会产生异常
        except:
            pass
        else:
            if len(recvdata)>0:
                print("%s:%s"%(str(clientinfo), recvdata))
            else:
                clientsocket.close()
                clientlist.remove((clientsocket, clientinfo))
                print("已下线%s"%str(clientinfo))
