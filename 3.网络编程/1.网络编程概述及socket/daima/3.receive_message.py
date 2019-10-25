from socket import *
# 创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口号
udpsocket.bind(('', 7788))
# 接受消息
recvdata = udpsocket.recvfrom(1024)
print(recvdata)