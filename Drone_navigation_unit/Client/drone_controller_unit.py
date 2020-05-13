import socket

msgFromClient = "Hello UDP Server"
serverIP = input("IP_ADDRESS_HERE: ")
serverPort = 20001
bufferSize = 1024

bytesToSend = str.encode(msgFromClient)

serverAddressPort = (serverIP, serverPort)

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)