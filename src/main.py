import FWTP

conn = FWTP.setupConnection()

url = "fwtp://fww.PaiShoFish49.me/games/sudoku"
dns = ('136.38.191.249', 5151)
URLdata = FWTP.extractURL(url)

FWTP.connect(conn, dns)
data = {
    "name": URLdata["hostName"],
    "tld": URLdata["tld"],
}
FWTP.transfer("DNSreq", data, conn)

hostAddr = tuple(FWTP.recieve(conn)["data"])
conn.close()

print(hostAddr)