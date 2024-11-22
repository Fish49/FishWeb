'''
fish web transfer protocol
'''

import socket
import json
import re

regexs = {
    "preamble": r"fwtps?://fww.",
    "hostName": r"[a-zA-Z0-9-\.]+",
    "tld":      r"\.(port|fun|me|fish|com|org)",
    "path":     r"(/[a-zA-Z0-9-\.]*)*",
    "flags":    r"(\?.+=.+(&.+=.+)*)?"
}

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

def extractURL(URL: str):
    if re.match(regexs["preamble"] + regexs["hostName"] + regexs["tld"] + regexs["path"] + regexs["flags"], URL) is None:
        raise Exception("invalid URL")

    URLre = re.search(f'(?P<preamble>{regexs["preamble"]})(?P<hostName>{regexs["hostName"]})(?P<tld>{regexs["tld"]})(?P<path>{regexs["path"]})(?P<flags>{regexs["flags"]})', URL)
    URLdict = URLre.groupdict()

    return URLdict["hostName"], URLdict["tld"], URLdict["path"], URLdict["flags"]

def webpageFromUrl(socket: socket.socket, URL: str, DNS: tuple[str, int]):
    # fwtp://fww.PaiShoFish49.port/games/sudoku

    socket.connect(DNS)
    data = {
        "transfer": "DNS",
        "data": extractURL(URL)[0]
    }
    socket.send(json.dumps(data).encode())

    hostAddr = json.loads(socket.recv(1024).decode())["data"]
    socket.close()

    socket.connect(hostAddr)
    data = {
        "transfer": "page",
        "data": {
            "path": extractURL(URL)[1]
        }
    }

print(extractURL("fwtp://fww.PaiShoFish49.port/games/sudoku?isLoggedIn=True&HasALife=False"))