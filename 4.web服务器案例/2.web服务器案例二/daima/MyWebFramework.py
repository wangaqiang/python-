import time

# from my_web_server import HTTPServer

# 设置静态目录
HTML_ROOT_DIR = "./1.html"

class Application(object):
    """web框架的核心部即框架的主体程序，框架是通用的"""
    def __init__(self, urls):
        self.urls = urls # 设置路由信息

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/") # 字典的get方法得不到时不会报错,保证了程序的容错率,第二个参数为默认值.
        # /static/jingtaiwenjan
        if path.startswith('/static'): # 访问静态文件
            file_name = path[7:]
            try:
                # 打开文件，读取内容
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found" # 返回响应体
            else:
                content = f.read()
                f.close()
        
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return content.decode('utf-8')

        for url, handler in self.urls:
            if url == path:
                return handler(env, start_response) # 将对应的路由处理结果即响应体返回

        # 如过路由表中没找到对应的路由,组建错误信息
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found" # 返回响应体


# 路由处理函数
def sayhello(env, start_response):
    """sayhello处理函数"""
    status = "200 OK"
    headers = []
    start_response(status, headers)
    return "hello kuangjia"


def show_ctime(env, start_response):
    """时间处理函数"""
    status = "200 OK"
    headers = []
    start_response(status, headers)
    return time.ctime()

urls = [
    ("/sayhello", sayhello)
]
app = Application(urls)

# if __name__ == "__main__":
#     urls = [
#         ("/sayhello", sayhello)
#     ]

#     app = Application(urls)
#     httpserver = HTTPServer(app)
#     httpserver.set_port(8989)
#     httpserver.start()