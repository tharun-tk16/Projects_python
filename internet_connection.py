import socket
import urllib
import urllib.request

# def internet():
#     tk=socket.gethostbyname(socket.gethostname())
#     if tk=="127.0.0.1":
#         return tk
#     else:
#         return tk

# import socket

# # Get the local hostname
# hostname = socket.gethostname()

# # Get the IP address of the local machine
# tk = socket.gethostbyname(hostname)

# # Check if the IP address is localhost (127.0.0.1)
# if tk == "127.0.0.1":
#     print("No " + tk)
# else:
#     print("Yes " + tk)

def internet():
    if urllib.request.urlopen('https://google.com'):
        return "conneted"
    else:
        return "Not connected"
