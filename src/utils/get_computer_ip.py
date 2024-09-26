import socket


def get_computer_ip():
    return socket.gethostbyname(socket.gethostname())
