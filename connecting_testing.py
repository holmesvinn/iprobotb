import os
from socket import *
host = "raspberrypi" # set to IP address of target computer
port = 13000
buff = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
data = input("Enter message to send or type 'exit': ")
UDPSock.sendto(data.encode(), addr)
(data,addr) = UDPSock.recvfrom(buff)
print(data)
if data == "exit":
    UDPSock.close()
    os._exit(0)



#forward = fwd
#reverse = rev
#left = left
#right = right
#up = up
#down = down
