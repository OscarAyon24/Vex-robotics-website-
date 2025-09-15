import os
from framework import Server, ResponseData

server = Server(port=8081)

@server.get("/")
def main(_, __):
    return ResponseData(ResponseData.ResponseCode.OK).appendHeader(ResponseData.Header("Content-Type", "text/html")).appendData(open("./site_data/index.html", "r", encoding="utf-8").read())

@server.get("/file")
def fileEndpoint(_, data: dict[str, str]):
    if not data.__contains__('file'): return ResponseData(ResponseData.ResponseCode.BAD_REQUEST)
    elif not data['file'].endswith(".json"): return ResponseData(ResponseData.ResponseCode.UNAUTHORIZED)
    elif not os.path.exists("./site_data/" + data["file"]): return ResponseData(ResponseData.ResponseCode.NOT_FOUND)
    else: return ResponseData(ResponseData.ResponseCode.OK).appendHeader(ResponseData.Header("Content-Type", {"json": "application/json"}[data["file"].split(".")[-1]])).appendData(open("./site_data/" + data["file"], "r", encoding="utf-8").read())

server.listen()