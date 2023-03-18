#import ncupdate
import requests
import miniupnpc

def my_public_ip():
    u = miniupnpc.UPnP()
    u.discoverdelay = 200
    u.discover()
    u.selectigd()
    return u.externalipaddress()


def main():
    print("Dyndns from local.")
    public_ip=my_public_ip()
    ncupdate.updateDomaine(public_ip)


if __name__ == "__main__":
    main()


