import ncupdate
import requests
import miniupnpc
import argparse


def my_public_ip():
    u = miniupnpc.UPnP()
    u.discoverdelay = 200
    u.discover()
    u.selectigd()
    return u.externalipaddress()


def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('opt_pos_arg', type=str, nargs='?',
                        help='A optional  extern ip.')

    args = parser.parse_args()
    public_ip = args.opt_pos_arg

    if public_ip is None:
        public_ip = my_public_ip()

    print("Dyndns from local extern ip: " + public_ip)
    ncupdate.updateDomaine(public_ip)


if __name__ == "__main__":
    main()
