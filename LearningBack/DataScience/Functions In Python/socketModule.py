import socket

def test():
    ip=socket.gethostbyname(socket.gethostname())
    return ip


print(test())

# shut down a system

