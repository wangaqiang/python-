from socket import *
#创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口
udpsocket.bind(('', 7788))
# 发送数据
udpsocket.sendto(b"haha", ('10.118.41.63', 2426))