import socket

hostn=socket.gethostname()
IPAd=socket.gethostbyname(hostn)
print("Our ip adress is :" + IPAd)