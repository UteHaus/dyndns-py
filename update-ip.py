import socket
import urllib.request
import fritzconnection as fc
from fritzconnection import FritzStatus
import sys

fritzPassword = 'F2!L16=f&f'
domain = 'wobco.de'
print(str(sys.argv))
fs = FritzStatus(password=fritzPassword)
if (fs.is_connected):
    print('FritzBox is connected')
    domainIp = socket.gethostbyname(domain)
    fritzboxIp = fs.external_ip

    if (domainIp == fritzboxIp):
        print('Domain and FritzBox Ips ara same')
        print('domain ip: ' + domainIp)
        print('fritzbox ip' + fritzboxIp)
    else:
        updateNetcup(fritzboxIp)


def checkip(fs, ):
    print('Ip Check for')
    print('my ip ')


def updateNetcup(ip):
    print('update netcup ip with:' + ip)
