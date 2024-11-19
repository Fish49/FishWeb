'''
fish web transfer protocol
'''

import socket

def setupClientConnection():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)