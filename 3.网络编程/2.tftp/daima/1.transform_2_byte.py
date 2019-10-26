import struct
from socket import *

data = struct.pack("!H8sb5sb", 1, "test.jpg", 0, "octet", 0)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(data, ("10.114.26.7",  69))

udp_socket.close()
