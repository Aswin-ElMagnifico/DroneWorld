import socket
import keyboard
import Drone_navigation_unit.Client.constants as movement_constants
from Drone_navigation_unit.Client.keypress_detection import get_key_pressed
import Drone_navigation_unit.Client.network_utilities as nw_util
from os import system

serverIP = input("IP_ADDRESS_HERE: ")
serverPort = 20001
bufferSize = 1024

serverAddressPort = (serverIP, serverPort)

# Create a UDP socket at client side
UDPClientSocket = nw_util.initialize_connection()


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
        nw_util.transmit(UDPClientSocket, serverAddressPort, keyPressed)
        system("sleep 1")
    else:
        if not loopControllerFallthrough:
            print("Auto-pilot")
            loopControllerFallthrough = True
