from socket import *


def main():
    udpsocket = socket(AF_INET, SOCK_DGRAM)
    udpsocket.bind(("", 9876))
    while True:
        data = udpsocket.recvfrom(1024)
        content, source = data
        print("%s:%s"%(str(source), content.decode("gb2312")))


if __name__ == "__main__":
    main()