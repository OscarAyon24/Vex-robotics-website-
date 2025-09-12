from framework import Server, ResponseData

server = Server()

@server.get("/")
def main(_, __, ___):
    return ResponseData(ResponseData.ResponseCode.OK).appendHeader(ResponseData.Header("Content-Type", "text/html")).appendData(open("./site_data/index.html", "r").read())

server.listen()