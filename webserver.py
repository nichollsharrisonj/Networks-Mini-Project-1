# Import socket module
from socket import *
import time
# Prepare server socket
# SOCK_STREAM for TCP, SOCK_DGRAM for UDP
ipaddress = gethostbyname(gethostname())


serverSocket = socket(AF_INET, SOCK_STREAM)
# Your code starts here
serverPort = 12000
serverSocket.bind((ipaddress, serverPort))
# serverSocket.bind(('174.204.205.50',serverPort))
serverSocket.listen(1)
print('Server is ready to receive')
#Your code ends here
while True:
    # Establish connection
    print('Server listening...')
    connectionSocket, addr = serverSocket.accept() # Your code starts here # Your code ends here
    print("accepted")
    try:
        message = connectionSocket.recv(1024)# Your code starts here # Your code ends here
        filename = message.split()[1]
        f = open(filename[1:])

        print("opened file")

        header = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n'

        outputdata = f.read()# Your code starts here # Your code ends here
        # outputdata = prepend + outputdata
        # Send one HTTP header line to socket
        # Your code starts here
        # connectionSocket.send(header.encode())


        # Your code ends here

        #Send object to client
        connectionSocket.sendall(header.encode() + outputdata.encode())
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        #     print("looping")
        # print("DONE looping")
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print("done")

    except IOError as e:
        print(e)

        htmlstring = "<html><h1></h1><body>404 not found</body></html>"
        err = "HTTP/1.0 404 Not Found\r\n\r\n" + htmlstring
        connectionSocket.send(err.encode())

        connectionSocket.close()
        # Send 404 message
        # Your code starts here

        # Your code ends here

        # Close client socket
        # Your code starts here

        # Your code ends here
serverSocket.close()
