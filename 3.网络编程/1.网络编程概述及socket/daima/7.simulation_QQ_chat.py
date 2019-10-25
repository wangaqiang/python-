from threading import Thread
from socket import *


#1收数据
def recvData():
    while True:
        recvinfo = udpsocket.recvfrom(1024)
        print(">>%s:%s"%(recvinfo[1], recvinfo[0].decode("gb2312")))

#2发数据
def sendData():
    while True:
        data = input("<<")
        udpsocket.sendto(data.encode("gb2312"), (destip, destport))

udpsocket = None
destip = ''
destport = 0

def main():
    global destip
    global destport
    global udpsocket
    
    destip = input("请输入目的IP：")
    destport = int(input("请输入目的IP："))

    udpsocket = socket(AF_INET, SOCK_DGRAM)
    
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == "__main__":
    main()