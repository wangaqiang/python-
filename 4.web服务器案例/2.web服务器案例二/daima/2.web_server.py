import re

from socket import *
from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./1.html"


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)#收到的是字节串不是字符串
    request_lines_list = request_data.splitlines()

    # 从"GET / HTTP/1.1"中提取客户端请求文件
    # 对获取到的数据进行提取
    request_start_line = request_lines_list[0]
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
    
    # 设置默认情况
    if "/" == file_name:
        file_name = "/index.html"
    try:
        # 打开文件，读取内容
        f = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "THE CONTENT IS NOT FOUND"
    else:
        content = f.read()
        f.close()

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = content.decode("utf-8")
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向客户端响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭客户端套接字
    client_socket.close()

if __name__ == "__main__":
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 设置多次使用
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
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