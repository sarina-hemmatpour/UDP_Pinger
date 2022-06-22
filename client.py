from encodings import utf_8
from http import server
import socket
import time


print("Starting ...")
#server="192.168.9.184"
server=socket.gethostbyname(socket.gethostname())
serverPort=5051
serverAddress=(server,serverPort)
seqNumber=0

#socket
clientSocket=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
#clientSocket.bind((host , port))

clientSocket.settimeout(1)



while seqNumber<10:

    try:
        startTime=time.time()

        data="udp_pinger"

        #sending
        clientSocket.sendto(data.encode(),serverAddress)

        #recieving
        data, address=clientSocket.recvfrom(2048)
   
        RTT=time.time()-startTime

        print("----------------")
        
        
        print(f"{seqNumber+1}-RTT: {RTT}")
        print(f"Data Recieved: {data.decode()}")

        

    except socket.timeout:
            print("----------------")
            print(f"{seqNumber+1}-_MESSAGE TIMEOUT_")

    
    seqNumber=seqNumber+1

print("Closing Socket")
clientSocket.close()