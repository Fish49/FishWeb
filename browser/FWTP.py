'''
fish web transfer protocol
'''

import socket
import json

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
    socket.send(json.dumps(message))