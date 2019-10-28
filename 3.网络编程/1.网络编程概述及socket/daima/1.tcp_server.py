from socket import *

serversocket = socket(AF_INET, SOCK_STREAM)
port = int(input("请为本程序输入端口号："))
serversocket.bind(('', port))

serversocket.listen(5)

clientsocket, clientinfo = serversocket.accept()

clientdata = clientsocket.recv(1024)

print("%s:%s"%(str(clientinfo), clientdata.decode("gb2312")))

clientsocket.close()

serversocket.close()