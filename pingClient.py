# ping client
from socket import *
import time

serverName = gethostbyname(gethostname())
serverPort = 12000

# create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for a sentence of input
message = input('Input a sentence in lowercase:')

numReceived = 0
numPings = 10
totalTime = 0
for i in range(numPings):
	start = time.time() #log start time

	clientSocket.sendto(message.encode(), (serverName, serverPort)) #send message

	receivedMessage, serverAddress = clientSocket.recvfrom(1024) #receive message

	pingTime = time.time() - start #calculate time taken

	decoded = receivedMessage.decode()

	if decoded == '': #received an empty string, which my server sends to simulate not returning a ping
		print("*\n") 
	else:
		print(f'Received message: {decoded}') #received an actual ping
		print(f'RTT: {pingTime}\n')
		numReceived += 1
		totalTime += pingTime

print(f'Packet loss rate: {(numPings-numReceived)/numPings}') #report data
print(f'Average RTT for returned packets: {totalTime/numReceived} seconds')
clientSocket.close()




