from requests import request


def get_public_ip():
    ip = request("GET", "https://api.ipify.org").text
    return ip
