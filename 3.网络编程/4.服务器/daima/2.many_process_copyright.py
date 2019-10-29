from socket import *
from multiprocessing import Process
        
def task(clientsocket, clientinfo):
    while True:
        recvdata = clientsocket.recv(1024)
        if len(recvdata) > 0:
            print("%s:%s"%(str(clientinfo), recvdata))
        else:
            break
    clientsocket.close()
    
def main():
    # 1创建套接字
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 2绑定套接字
    serversocket.bind(("", 6789))
    # 3设置为被动套接字
    serversocket.listen(6)
    try:
        while True:
            # 4接受客户端的链接
            clientsocket, clientinfo = serversocket.accept()
            p = Process(target=task, args=(clientsocket, clientinfo))
            p.start()
            clientsocket.close()
    finally:
        serversocket.close()

            
if __name__ == "__main__":
    main()