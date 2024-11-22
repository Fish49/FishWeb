'''
fish web transfer protocol
'''

import socket
import json
import re

def setupClientConnection(IP = '0.0.0.0', port = 5154, useUDP = False):
    if useUDP:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((IP, port))
    return s

def sendProgData(data, socket: socket.socket):
    message = {
        "tranfer": "progData",
        "data": data
    }
    socket.send(json.dumps(message).encode())

def webpageFromUrl(socket: socket.socket, URL: str, DNS: tuple[str, int]):
    # fwtp://fww.PaiShoFish49.port/games/sudoku
    host = re.search(r"")

    socket.connect(DNS)
    data = {
        "transfer": "DNS",
        "data": URL
    }
    socket.send(json.dumps(data).encode())

    hostAddr = json.loads(socket.recv(1024).decode())["data"]
    socket.close()

    socket.connect(hostAddr)
    data = {
        "transfer": "page",
        "data": {
            "path": "/"
        }
    }