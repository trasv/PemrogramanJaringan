import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port_num = 8888
server_address = ('127.0.0.1', port_num)
print("Connecting to Server: 127.0.0.1" , " Port:", port_num)
sock.connect(server_address)

try:
    filename = "cobain.txt"
    temp = open(filename, "rb")
    file = temp.read(2048)
    temp.close()
    file = file.decode()
    messg = "add " + filename+" " + file
    messg_enc = messg.encode()
    sock.send(messg_enc)
    print("Adding File")
    data = sock.recv(2048).decode()

finally:
    print("Closing Connection")
    sock.close()