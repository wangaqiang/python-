from socket import *
# 1创建套接字
udpsocket = socket(AF_INET, SOCK_DGRAM)
# 2调用sendto发送
udpsocket.sendto("haha", ("10.118.41.63", 8080))