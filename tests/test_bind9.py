from ipaddress import IPv4Address
import os
import yaml
import pytest

def test_dns_data_exists():
    dns_data_path = "../data/bind9/dns.yaml"
    assert os.path.isfile(dns_data_path)

def test_dns_data_sorted():

    # Load the YAML file
    with open('../data/bind9/dns.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    # Sort the records based on the 'ip' key after converting to int
    sorted_data = sorted(data['dns_records'], key=lambda x: int(IPv4Address(x['ip'])))
    
    for pos, record in enumerate(data['dns_records']):
        ip = record.get('ip')
        if sorted_data[pos].get('ip') == ip:
            continue
        else:
            pytest.fail(f"Record at position {pos} is not sorted correctly: expected {sorted_data[pos].get('ip')}, got {ip}")

    assert True # Explicit success if no failure cases found