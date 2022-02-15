# ping client
from socket import *
import time

serverName = gethostbyname(gethostname()) #get ip
serverPort = 12000

# create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for a sentence of input
message = input('Input a sentence in lowercase:')

numReceived = 0
numPings = 10
totalTime = 0
clientSocket.settimeout(1.) #Use socket timeout method
for i in range(numPings):
	try:
		start = time.time() #log start time

		clientSocket.sendto(message.encode(), (serverName, serverPort)) #send message

		receivedMessage, serverAddress = clientSocket.recvfrom(1024) #receive message

		pingTime = time.time() - start #calculate time taken

		decoded = receivedMessage.decode()
	 
		print(f'Received message: {decoded}') #received an actual ping
		print(f'RTT: {pingTime}\n')
		numReceived += 1
		totalTime += pingTime
		
	except timeout: #Timed out, print * symbol and go on to next ping
		print('*')

lossrate = ((numPings- numReceived)/numPings)
avgrtt = (totalTime/numReceived)

print(f'Packet loss rate: {lossrate}') #report data
print(f'Average RTT for returned packets: {avgrtt} seconds')
clientSocket.close() #close connection




