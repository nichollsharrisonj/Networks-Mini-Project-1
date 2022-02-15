# UDP Ping Server
# Using random to simulate packet loss
import random
# Import socket module
from socket import *
import time

#randomly set the chance of failing before running the server
failChance = .5


serverIp = gethostbyname(gethostname()) #set ip
print(f"ip is: {serverIp}")

serverSocket = socket(AF_INET, SOCK_DGRAM) # SOCK_STREAM for TCP, SOCK_DGRAM for UDP
print("made socket")

serverSocket.bind((serverIp, 12000)) # Assign IP address and port number to socket
print("bound socket")

while True:

    message, address = serverSocket.recvfrom(1024) #Receive client packet and arrival address

    
    message = message.decode().upper() #Capitalize the message, to simulate a ping going through

    if random.random() < failChance: #Decide at random, with probability decided earlier, whether or not to return packeg
        serverSocket.sendto(message.encode(), address)
    else:
        time.sleep(1)
        # serverSocket.sendto(''.encode(),address) #To simulate a ping not being returned, send an empty string.

    

