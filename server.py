import socket
serverAddress = "https://pythonserver.onrender.com"
PORT = 1024
numberOfBytes = 8

myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myTCPSocket.bind((serverAddress, PORT))
myTCPSocket.listen(5) # idk what the numbers mean
incomingSocket, incomingAddress = myTCPSocket.accept() # accepts any incoming messages

flag = True

while flag:
    print("Server Online")
    receivedData = incomingSocket.recv(numberOfBytes) # Output is a bytearray
    strData = str(receivedData,"utf-8") # trasnforms bytearray to string

    # Logic to upper all characters
    responseData = strData.upper()
    incomingSocket.send(bytearray(str(responseData), encoding="utf-8")) # sends new message back to client

    # flag = int(input("0 = False & 1 = True")) # allows to end loop

incomingSocket.close()
