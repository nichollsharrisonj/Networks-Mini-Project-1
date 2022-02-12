from socket import *
import sys
# IP address


serverName = str(input("Enter IP: "))
# Port number to use
serverPort = int(input("Enter port: "))
path = str(input("Enter path: "))
# Create socket for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect via our socket and port number to the IP
clientSocket.connect((serverName, serverPort))
# Ask user for a sentence to echo
getrequest = f'GET /{path} HTTP/1.1\r\nHost:{serverName}:{serverPort}\r\n\r\n'
# sentence = input('Input a sentence in lowercase:')
# Send user input sentence
clientSocket.send(getrequest.encode())
# Receive response from server via our socket
page = clientSocket.recv(1024).decode()
# Your code starts here # Your code ends here

# Display
print('\nMessage from server: \n\n' + page)

clientSocket.close()


# Create a super simple web client to go with your server. Your client should
# (a) take as input the server IP address, port at which the server listens, and object (with path) stored on the server
# (b) connect to the server using a TCP connection,
# (c) send an HTTP request with GET method to the server,
# (d) display server response message as output.

