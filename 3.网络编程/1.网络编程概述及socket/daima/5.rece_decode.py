from socket import *
udpsocket = socket(AF_INET, SOCK_DGRAM)
udpsocket.bind(("", 8989))
data = udpsocket.recvfrom(1024)
content, source = data
print(content.decode("gb2312"))