from socket import *
import sys
# IP address


serverName = input("Enter IP: ") #Get IP from user
serverPort = int(input("Enter port: ")) #Get port number from user
path = input("Enter path: ") #Get path of desired file from user

clientSocket = socket(AF_INET, SOCK_STREAM) #create socket for TCP
clientSocket.connect((serverName, serverPort)) #connect using socket and port number to the provided IP

getrequest = f'GET /{path} HTTP/1.1\r\nHost:{serverName}:{serverPort}\r\n\r\n' #Make getrequest string with proper http formatting

clientSocket.send(getrequest.encode()) #Send encoded version of getrequest
page = clientSocket.recv(1024).decode() # Receive response from server via our socket

print('\nMessage from server: \n\n' + page) #Display the message

clientSocket.close() #Close connection



