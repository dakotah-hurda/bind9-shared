import yaml
from ipaddress import IPv4Address
from pprint import pprint

def main():
    """This script is literally only used for sorting my DNS entries A->B. 
    """
    
    sorted_data = dict()

    # Load the YAML file
    with open('dns.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    # Sort the records based on the 'int' key
    sorted_data['dns_records'] = sorted(data['dns_records'], key=lambda x: int(IPv4Address(x['ip'])))

    # Output the sorted data
    pprint(f"Sorted Data:\n\n{sorted_data}")


    with open('dns.yaml', 'w') as f:
        yaml.dump(sorted_data, f, default_flow_style=False)

if __name__ == '__main__':
    main()
