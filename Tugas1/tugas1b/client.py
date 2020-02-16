import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    variabel = input("input ")
    print("sending file...")
    sock.sendall(variabel.encode())
    while 1:
        data = sock.recv(1024)
        file = open("fromserver_"+variabel,'wb')
        if not data:
            file.close()
            break
        file.write(data)
    print('received "%s"' % variabel)
finally:
    print ('closing socket')
    sock.close()