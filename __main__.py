import fritzconnection.lib.fritzstatus as fs
import ncupdate


def main():
    print("Dyndns from local.")

    ncupdate.updateDomaine(fs.FritzStatus().external_ip)


if __name__ == "__main__":
    main()
