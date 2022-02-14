# Import socket module
from socket import *
import time

ipaddress = gethostbyname(gethostname()) #get ip


serverSocket = socket(AF_INET, SOCK_STREAM) #This is for TCP protocol

serverPort = 12000
serverSocket.bind((ipaddress, serverPort)) #bind socket

serverSocket.listen(1) #listen

print('Server is ready to receive')

while True:
    # Establish connection
    print('Server listening...')
    connectionSocket, addr = serverSocket.accept() # Your code starts here # Your code ends here

    try:
        message = connectionSocket.recv(1024)  #receive message
        filename = message.split()[1] #figure out what file is being requested from message
        f = open(filename[1:]) #open it
        outputdata = f.read() #read it

        header = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n' #create OK http header

        connectionSocket.sendall(header.encode() + outputdata.encode()) #send the header and the file data
        
        connectionSocket.send("\r\n".encode()) #followed by new line and carriage return

        connectionSocket.close() #close the connection
        print("done")

    except IOError as e:
        print(e)

        htmlstring = "<html><h1></h1><body>404 not found</body></html>" #create 404 page
        err = "HTTP/1.0 404 Not Found\r\n\r\n"  #add 404 header
        connectionSocket.send(err.encode() + htmlstring.encode()) # Send 404 message
        connectionSocket.close() #close connection

serverSocket.close()
