from socket import *
from threading import Thread

def task(clientsocket, clientinfo):
    while True:
        recvdata = clientsocket.recv(1024)
        if len(recvdata)>0:
            print("%s:%s"%(str(clientinfo), recvdata))
        else:
            break
    clientsocket.close()

def main():
    # 1创建套接字
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 2绑定
    serversocket.bind(("", 6789))
    # 3设置为被动套接字
    serversocket.listen(5)
    try:
        while True:
            clientsocket, clientinfo = serversocket.accept()
            t = Thread(target=task, args=(clientsocket, clientinfo))
            t.start()
    finally:
        serversocket.close()


if __name__ == "__main__":
    main()