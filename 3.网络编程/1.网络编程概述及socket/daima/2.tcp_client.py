from socket import *

clientsocket = socket(AF_INET, SOCK_STREAM)

clientsocket.connect(("192.168.242.1", 8888))

clientsocket.send("haha".encode("gb2312"))

recvdata = clientsocket.recv(1024)

print("%s"%recvdata.decode("gb2312"))