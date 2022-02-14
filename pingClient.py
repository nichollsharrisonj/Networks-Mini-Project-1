# ping client
from socket import *
import time

serverName = '134.10.73.65'#gethostbyname(gethostname())
serverPort = 12000

# create socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# Ask user for a sentence of input
message = input('Input a sentence in lowercase:')

numReceived = 0
numPings = 10
totalTime = 0
for i in range(numPings):
	# Use socket to send message, note the use of encode() and the address
	start = time.time()

	clientSocket.sendto(message.encode(), (serverName, serverPort))
	# Receiving follows similar format, 2048 is buffer size for input
	receivedMessage, serverAddress = clientSocket.recvfrom(1024)

	pingTime = time.time() - start

	decoded = receivedMessage.decode()
	if decoded == '': #received an empty string, which my server sends to simulate not returning a ping
		print("*\n") 
	else:
		print(f'Received message: {decoded}')
		print(f'RTT: {pingTime}\n')
		numReceived += 1
		totalTime += pingTime

print(f'Packet loss rate: {(numPings-numReceived)/numPings}')
print(f'Average RTT for returned packets: {totalTime/numReceived} seconds')
clientSocket.close()




