# UDP Ping Server
# Using random to simulate packet loss
import random
# Import socket module
from socket import *


#randomly set the chance of failing
failChance = random.random()

#set ip
serverIp = gethostbyname(gethostname())
print(f"ip is: {serverIp}")
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
    message = message.decode().upper()
    print(message)
    # Error simulator goes here
    # Your code starts here
    if random.random() < failChance:
        serverSocket.sendto(message.encode(), address)
    else:
        serverSocket.sendto(''.encode(),address)
    # Your code ends here
    # If no error, server responds
    

