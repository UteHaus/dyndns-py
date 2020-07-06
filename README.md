# dyndns-py

## API

Use the following API [nc_dnsapi](https://github.com/nbuchwitz/nc_dnsapi) to update DNS records.

### Install Dependencies:

For default python version:

```sh
    pip install fritzconnection
```

or for specific python version:

```sh
    pip3 install fritzconnection
```

### Troubleshooting

**python**
- `ModuleNotFoundError: No module named 'fritzconnection'` reintall `fritzconnection`

## Start

1. install python3 `sudo apt install python3`
1. In the folder run `git clone https://github.com/nbuchwitz/nc_dnsapi`
1. `mv nc_dnsapi api`
1. `python3 .`

## Important!!

The `host.json` and `settings.json` files must have a valide json format.
