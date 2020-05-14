import socket
import keyboard
import Drone_navigation_unit.Client.constants as movement_constants
from Drone_navigation_unit.Client.keypress_detection import get_key_pressed
from os import system

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


def update_command():
    flag = False
    for keys in movement_constants.KEY_LIST:
        if keyboard.is_pressed(keys):
            flag = True
            break
        else:
            flag = False
    return flag


# Starting simulation


loopControllerFallthrough = False;
while True:

    if update_command():
        loopControllerFallthrough = False
        keyPressed = get_key_pressed()
        print(keyPressed)
        system("sleep 1")
    else:
        if not loopControllerFallthrough:
            print("Auto-pilot")
            loopControllerFallthrough = True
