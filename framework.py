from typing import Literal
from enum import Enum
import threading
import socket

class Cookie:
    @classmethod
    def delete(cls, name: str, path: str = "/"):
        cls.cookie_name = name
        cls.value = ""
        cls.age = 0
        cls.path = path
        return cls
    @classmethod
    def set(cls, name: str, value: str, age: int = 86400, path: str = "/"):
        cls.cookie_name = name
        cls.value = value
        cls.age = age
        cls.path = path
        return cls
    @staticmethod
    def buildDict(cookies: list[str]):
        data = {}
        for cookie in cookies:
            data[cookie.split("=")[0]] = cookie.split("=")[1]
        return data
    def get(self) -> str:
        return f"Set-cookie: {self.cookie_name}={self.value}; Max-Age={self.age}; Path={self.path}\r\n"

class ResponseData:
    class ResponseCode(Enum):
        OK = "200 OK"
        NOT_FOUND = "404 Not Found"
        UNAUTHORIZED = "401 Unauthorized"
    class Header:
        def __init__(self, type: Literal["Content-Length", "Refresh"], data: int):
            self.output = type + ": " + data + "\r\n"
            pass
        def __init__(self, type: Literal["Content-Type", "Location"], data: str):
            self.output = type + ": " + data + "\r\n"
            pass
        def __init__(self, type: Literal["Set-Cookie"], data: Cookie):
            self.output = type + ": " + data.get() + "\r\n"
            pass
        def __init__(self, type: Literal["Content-Disposition"], data):
            self.output = type + ": " + data + "\r\n"
            pass
    def __init__(self, code: ResponseCode):
        self._code = code
        self.headers: list[ResponseData.Header] = []
        self.data = "".encode(encoding="utf-8")
    def appendHeader(self, header: Header):
        self.headers.append(header)
        return self
    def appendData(self, data: bytes):
        self.data += data
        return self
    def appendData(self, data: str):
        self.data += data.encode(encoding="utf-8")
        return self
    def build(self) -> bytes:
        returnData: bytes = ("HTTP/1.1 " + self._code.value + "\r\n").encode()
        for header in self.headers:
            returnData += header.output.encode(encoding="utf-8")
        returnData += "\r\n".encode(encoding="utf-8")
        return returnData + self.data

class Server:

    def __init__(self, host: str = '127.0.0.1', port: int = 443):
        self.gets = {}
        self.posts = {}

        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the host and port
        self.server_socket.bind((host, port))
        print(f"Server bound to {host}:{port}")
    def get(self, path: str):
        def _get(func):
            self.gets[path] = func
        return _get
    def post(self, path: str):
        def _post(func):
            self.posts[path] = func
        return _post
    @staticmethod
    def parse_data(data: str):
        data = data.split("&")
        output = {}
        for item in data:
            output[item.split("=")[0]] = item.split("=")[1]
        return output
    @staticmethod
    def recieve_data(socket: socket.socket):
        headers = socket.recv(1024).decode('utf-8')
        data = {}
        cookies = {}

        if "\r\n\r\n" in headers and "Content-Length: " in headers:
            length = int(headers.split("Content-Length: ")[1].split("\r\n")[0])
            if len(headers.split("\r\n\r\n")) > 1:
                content = headers.split("\r\n\r\n")[1]
            else: content = ""
            while len(content) < length:
                content += socket.recv(1024).decode("utf-8")
            data = Server.parse_data(content)
        if headers.__contains__("Cookie: "):
            cookies = Cookie.buildDict(headers.split("Cookie: ")[1].split("\r\n")[0].split("; "))

        return headers, data, cookies, headers.split(" ")[0] == "GET"
    def listen(self):
        self.running = True

        # Start listening for incoming connections
        self.server_socket.listen(1)
        print("Server listening")

        listen_thread = threading.Thread(target=self.__server_loop)
        self.shutdown_flag = threading.Event()
        listen_thread.start()

        while not self.shutdown_flag.is_set():
            cmd = input()
            if cmd == "stop":
                self.shutdown_flag.set()
                self.server_socket.close()

    def __server_loop(self):
        while not self.shutdown_flag.is_set():
            try :
                # Accept a connection from a client
                client_socket, client_addr = self.server_socket.accept()

                # Receive the request data
                client_request, data, cookies, get = self.recieve_data(client_socket)

                request = client_request.split("\r\n")[0].split(" ")[1].split("?")

                if len(request) == 2: data = self.parse_data(request[1])

                print(f"Request for {request[0]} from {client_addr} with cookies {cookies} and data {data}\n")

                if get and request[0] in self.gets:
                    client_socket.sendall(self.gets[request[0]](cookies, data).build())
                elif not get and request[0] in self.posts:
                    client_socket.sendall(self.posts[request[0]](cookies, data).build())
                else:
                    html_data = open("./site_data/404.html", "r").read()
                    client_socket.sendall(f"HTTP/1.1 404 Not Found\nContent-type: text/html\n\n{html_data}".encode('utf-8'))
                
                client_socket.close()
            except OSError:
                continue
        print("Server shuting down")