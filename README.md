# dyndns-py for netcup

## API

Use the following API [nc_dnsapi](https://github.com/nbuchwitz/nc_dnsapi) to update DNS records.


### Troubleshooting

**python**
- `ModuleNotFoundError: No module named 'fritzconnection'` reintall `fritzconnection`

## Start

1. install python3 `sudo apt install python3 pip3` 
1. install `pip install miniupnpc`
1. `git clone https://github.com/UteHaus/dyndns-py.git`
1. switch in the folder `dyndns-py`
1. In the folder run `git clone https://github.com/nbuchwitz/nc_dnsapi`
1. `mv nc_dnsapi api`
1. `python3 .`

## Important!!

The `host.json` and `settings.json` files must have a valide json format.
