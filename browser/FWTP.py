'''
fish web transfer protocol
'''

import socket

class Listener():
    def __init__(self, isFromIp: True, client: str | socket.socket, onRecieve: function):
        if isFromIp:
            ipPort = client.split(":")
            self.ip = ipPort[0]
            if len(ipPort) > 1:
                self.port = ipPort[1]
        
        else:
            self.ip = socket._Address

        self.onRecieve = onRecieve

    

# def sendToIp(IP, data):


# def getIpFromURL(URL, DNS):
#     request

# def getPage()

socket.