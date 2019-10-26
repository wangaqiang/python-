from socket import *
import struct
    
def main():    
    filename = "test.jpg"
    f = open(filename, "w")
    filename_mount = len(filename)
    
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    send_data = struct.pack("!H%dsb5sb"%filename_mount, 1, filename, 0, "octet", 0)
    udp_socket.bind(("", 5678))
    udp_socket.sendto(send_data, ("10.118.122.128", 69))
    
    while True:
        recv_data = udp_socket.recvfrom(1024)
        re_info, re_ip_port_tuple = recv_data
        opcode_and_block_tuple = struct.unpack("!HH", re_info[0:4])
    
        if opcode_and_block_tuple[0] == 3:
            f.write(re_info[4:])
    
            send_ack = struct.pack("!HH", 4, opcode_and_block_tuple[1])
            udp_socket.sendto(send_ack, re_ip_port_tuple)
            if len(re_info)<516:
                break
    f.close()

if __name__ == "__main__":
    main()