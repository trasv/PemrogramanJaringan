import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    variabel="IMG20170525134042.jpg"
    variabel1 = open (variabel, "rb")
    variabel2 = variabel1.read()
    print("sending file...")
    sock.sendall(variabel2)
finally:
    print("closing socket")
    sock.close()