# UDP Ping Server
# Using random to simulate packet loss
import random
# Import socket module
from socket import *

#set ip
serverIp = gethostbyname(gethostname())
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)
print("made socket")
# Assign IP address and port number to socket
serverSocket.bind((serverIp, 12000))
print("bound socket")

while True:
    # Receive client packet and arrival address
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message
    message = message.upper()
    # Error simulator goes here
    # Your code starts here

    # Your code ends here
    # If no error, server responds
    serverSocket.sendto(message, address)

