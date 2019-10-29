from socket import *
from multiprocessing import Process


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request_data:", request_data)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello itcast"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response_data:", response)

    # 向客户端响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端套接字
    client_socket.close()

if __name__ == "__main__":
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定套接字
    server_socket.bind(("", 8989))
    # 监听套接字
    server_socket.listen(128)
    # 创建多进程
    while True:
        client_socket, client_info = server_socket.accept()
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
