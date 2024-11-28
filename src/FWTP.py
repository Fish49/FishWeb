'''
fish web transfer protocol
'''

import socket
import json
import re
import threading
import ssl

def dataIsComplete(data: str):
    if data.count("}") >= data.count("{"):
        return True
    return False

def receive(socket: socket.socket):
    data = socket.recv(1024).decode()
    while dataIsComplete(data) is False:
        chunk = socket.recv(1024)
        if not chunk:
            break

        data += chunk.decode()

    return json.loads(data)

def setupConnection(IP = '0.0.0.0', port = 5154, useUDP = False):
    if useUDP:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((IP, port))
    return s

def transfer(transferType: str, data, socket: socket.socket):
    transferData = {
        "transfer": transferType,
        "data": data
    }
    socket.send(json.dumps(transferData).encode())

def connect(socket: socket.socket, addr: tuple[str, int]):
    socket.connect(addr)

def extractURL(URL: str):
    regexs = {
        "preamble": r"fwtps?://fww.",
        "hostName": r"[a-zA-Z0-9-\.]+",
        "tld":      r"\.(port|fun|me|fish|com|org)",
        "path":     r"(/[a-zA-Z0-9-\.]*)*",
        "flags":    r"(\?.+=.+(&.+=.+)*)?"
    }

    if re.match(regexs["preamble"] + regexs["hostName"] + regexs["tld"] + regexs["path"] + regexs["flags"], URL) is None:
        raise Exception("invalid URL")

    URLre = re.search(f'(?P<preamble>{regexs["preamble"]})(?P<hostName>{regexs["hostName"]})(?P<tld>{regexs["tld"]})(?P<path>{regexs["path"]})(?P<flags>{regexs["flags"]})', URL)
    URLdict = URLre.groupdict()

    return URLdict

def webpageFromUrl(socket: socket.socket, URL: str, DNS: tuple[str, int]):
    # fwtp://fww.PaiShoFish49.me/games/sudoku
    URLdata = extractURL(URL)

    connect(socket, DNS)
    data = {
        "name": URLdata["hostName"],
        "tld": URLdata["tld"],
    }
    transfer("DNSreq", data, socket)

    hostAddr = tuple(receive(socket)["data"])
    socket.close()

    connect(socket, hostAddr)
    data = {
        "path": URLdata[2],
        "flags": URLdata[1]
    }
    transfer("pagereq", data, socket)

    response = receive(socket)
    return response["data"]

def handleConnections(onConnection, socket: socket.socket, disconnect = lambda: False):
    socket.listen(1)
    while True:
        if disconnect() is True:
            break
        conn, addr = socket.accept()
        threading.Thread(target=onConnection, args=(conn,)).start()