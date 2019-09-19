import socket
import urllib.request

print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname("wobco.de"))

# get my public ip
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(external_ip)


# get infos from fritzbox https://pypi.org/project/fritzconnection/
