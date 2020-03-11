import fritzconnection as fc
import ncupdate


# install fritzbox
# install pip3 install dnslib
# pip3 install urllib5
# pip3 install tabulate

def main():
    ncupdate.updateDomaine(fc.FritzStatus().external_ip)


if __name__ == "__main__":
    main()
