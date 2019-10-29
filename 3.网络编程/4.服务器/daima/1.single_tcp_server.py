from socket import *
# 1.创建套接字
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR ,1)
# 2.绑定套接字
serversocket.bind(("" ,6789))
# 3.设置为被动套接字
serversocket.listen(5)
while True:
    # 4.设置为接听
    clientsocket, clientinfo = serversocket.accept()
    print("主进程接下来处理数据%s"%str(clientinfo))
    try:
        while True:
            recvdata = clientsocket.recv(1024)
            if len(recvdata) > 0:
                print("来自%s:%s"%(str(clientinfo), recvdata))
            else:
                break
    finally:
        clientsocket.close()
serversocket.close()