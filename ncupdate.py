import json
from api.nc_dnsapi import DNSRecord, Client
import socket


def updateDomaine(currentIp: str):
    host = getHostDefinition()
    subDomains = getJsonRecords(host['hosts'])
    settings = getSettings()
    domain = host['zone']['domainname']
    with getClientSettings(settings) as client:

        print("Check IP table for " + domain)
        printZoneInformation(client, domain)
        dnsRecords = getDnsRecords(client, domain)
        for subDomain in subDomains:
            checkDnsRecord(client, domain, findRecord(
                subDomain, dnsRecords), subDomain, currentIp)


def checkDnsRecord(client: Client, domain: str, dnsRecord: DNSRecord, settingDnsRecord: DNSRecord, currentIp: str):
    if (dnsRecord):
        if (dnsRecord.destination != currentIp):
            print("Update settings of " + dnsRecord.hostname + ".")
            setIp(dnsRecord, currentIp)
            client.update_dns_record(domain, dnsRecord)
        else:
            print("Settings of " + dnsRecord.hostname + " are up to date.")

        printIp(dnsRecord.destination, currentIp)
    else:
        print('For the subdomain ' + settingDnsRecord.hostname +
              ' find any dns record, create a new.')
        setIp(settingDnsRecord, currentIp)
        printIp(settingDnsRecord.destination, currentIp)
        client.add_dns_record(domain, [settingDnsRecord])


def printIp(currentIp: str, newIp: str):
    print("current Ip: " + currentIp)
    print("new ip: " + newIp)


def setIp(dnsRecord: DNSRecord, currentIp: str) -> DNSRecord:
    if (is_valid_ipv4_address(dnsRecord.destination)):
        dnsRecord.destination = currentIp
    return dnsRecord


def findRecord(settingDnsRecord: DNSRecord, dnsRecords: [DNSRecord]) -> DNSRecord:
    for record in dnsRecords:
        if (record.hostname == settingDnsRecord.hostname):
            return record

    return None


def hasSameIp(record, ip: str):
    return record.destination == ip


def getClientSettings(settings) -> Client:
    return Client(settings["CUSTOMER_ID"], settings["API_KEY"], settings["API_PASSWORD"])


def getSettings():
    with open("settings.json") as fp:
        settings = json.load(fp)
    return settings


def getHostDefinition():
    with open('hosts.json') as fp:
        hosts = json.load(fp)

    return hosts


def printZoneInformation(api: Client, domain: str):
    zone = api.dns_zone(domain)
    print(zone)


def getDnsRecords(api: Client, domain: str):
    return api.dns_records(domain)


def getJsonRecords(jsonRecords) -> [DNSRecord]:
    records = []
    for record in jsonRecords:
        newRecord = DNSRecord(getKeyValue(record, 'hostname'), getKeyValue(record, 'type'),
                              getKeyValue(record, 'destination'))
        records.append(newRecord)

    return records


def getKeyValue(data, key: str) -> str:
    try:
        return data[key]
    except:
        return None


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
