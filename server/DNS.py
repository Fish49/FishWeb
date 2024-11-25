import FWTP
import json

conn = FWTP.setupConnection(port=5151)

def register(name, tld, IP, port):
    with open('server/DNSdb.json', 'rw') as file:
        dbdict = json.load(file)

        cond1 = not (name in dbdict[tld].keys())
        cond2 = isinstance(port, int)
        cond3 = isinstance(IP, str)
        if cond1 and cond2 and cond3:
            dbdict[tld][name] = [IP, port]

        json.dump(dbdict, file)

def handleRequest(socket: FWTP.socket.socket):
    data = FWTP.recieve(socket)
    if data["transfer"] == "DNSreq":
        with open("DNSdb.json", 'r') as file:
            dbdict = json.load(file)

        print(data)
        FWTP.transfer("DNSres", dbdict[data["data"]["tld"][1:]][data["data"]["name"]], socket)

    socket.close()

FWTP.handleConnections(handleRequest, conn)