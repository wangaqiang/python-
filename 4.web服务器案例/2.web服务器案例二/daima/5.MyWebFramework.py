from my_web_server import HTTPServer

class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/")
        for url, handler in self.urls:
            if url == path:
                return handler(env, start_response)
        status = "404 NOT FOUND"
        headers = []
        start_response(status, headers)
        return "not found"

def sayhello(env, start_response):
    status = "200 OK"
    headers = []
    start_response(status, headers)
    return "hello kuangjia"

if __name__ == "__main__":
    urls = [
        ("/sayhello", sayhello)
    ]

    app = Application(urls)
    httpserver = HTTPServer(app)
    httpserver.set_port(8989)
    httpserver.start()