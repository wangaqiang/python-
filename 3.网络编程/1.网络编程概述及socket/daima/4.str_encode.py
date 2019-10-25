from socket import *
udpsocket = socket(AF_INET, SOCK_DGRAM)
ip = input("请输入目的IP：")
port = int(input("请输入端口号："))
data = input("请输入发送的内容：")
udpsocket.sendto(data.encode("gb2312"), (ip, port))