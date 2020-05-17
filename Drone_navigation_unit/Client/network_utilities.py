import socket


def initialize_connection():
    return socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


def transmit(socket_id, server_address, command):
    command = str.encode(command)
    socket_id.sendto(command, server_address)
