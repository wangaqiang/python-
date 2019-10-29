import re

from socket import *
from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./1.html"

class HTTPServer(object):
    """web服务器类"""
    def __init__(self):
    # 1.初始化服务器
        # 创建套接字
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 设置多次使用
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self):
        """启动服务器方法"""
        # 监听套接字
        self.server_socket.listen(128)
        while True:
            client_socket, client_info = self.server_socket.accept()
            # 创造子进程进行接受消息
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
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

    def set_port(self, port):
        """给新创建的对象绑定端口号"""
        # 绑定套接字
        self.server_socket.bind(("", port))
        

    
def main():
    # 创建服务器对象
    http_server = HTTPServer()
    # 调用绑定端口号的方法
    http_server.set_port(8989)
    # 启动服务器
    http_server.start()

if __name__ == "__main__":
   main()