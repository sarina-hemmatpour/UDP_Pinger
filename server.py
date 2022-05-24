from operator import truediv
import socket

#server="192.168.9.184"
serverPort=5051
server=socket.gethostbyname(socket.gethostname())

#print(server)

#socket
serverSocket=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

serverSocket.bind((server , serverPort))

print("The server is ready to recieve")

while True:
    data, clientAddress=serverSocket.recvfrom(2048)
    data=data.decode().upper()

    #sendback
    serverSocket.sendto(data.encode() , clientAddress)
    
