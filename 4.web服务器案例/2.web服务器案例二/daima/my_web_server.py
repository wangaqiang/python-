import re
import sys

from socket import *
from multiprocessing import Process

# 设置静态文件根目录
HTML_ROOT_DIR = "./1.html"

WSGI_PYTHON_DIR = "./wsgipython"

class HTTPServer(object):
    """web服务器类"""
    def __init__(self, app):
    # 1.初始化服务器
        # 创建套接字
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        # 设置多次使用
        self.server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = app

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
        
    def start_response(self, status, headers):
        """
        status = "200 OK"
        headers = [
            ("Content-Type", "text/plain")
        ]
        """
        # 构建响应头
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers
        
    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)#收到的是字节串不是字符串
        request_lines_list = request_data.splitlines()
    
        # 从"GET / HTTP/1.1"中提取客户端请求文件
        # 对获取到的数据进行提取
        request_start_line = request_lines_list[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1) #返回值为字符串
        
        env = {"PATH_INFO": file_name} # 字典 存放解析到的其他东西
        response_body = self.app(env, self.start_response)

        # 构造响应数据
        response = self.response_headers + "\r\n" + response_body
    
        # 向客户端响应数据
        client_socket.send(bytes(response, "utf-8"))
    
        # 关闭客户端套接字
        client_socket.close()

    def set_port(self, port):
        """给新创建的对象绑定端口号"""
        # 绑定套接字
        self.server_socket.bind(("", port))
        

    
def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    # 创建服务器对象
    http_server = HTTPServer()
    # 调用绑定端口号的方法
    http_server.set_port(8989)
    # 启动服务器
    http_server.start()

if __name__ == "__main__":
    main()