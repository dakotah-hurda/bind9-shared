import yaml
from jinja2 import Environment, FileSystemLoader
import os
   
def main():
    
    # Should replace this with Netbox in the future.
    data_file = 'dns.yaml'
    with open(data_file, 'r') as file:
        data = yaml.safe_load(file)

    # Generates PTR records.
    for record in data['dns_records']:
        ip = record['ip']
        octets = ip.split(".")
        ptr = f"{octets[3]}.{octets[2]}" # assumes single-zone "192.168.."
        record['ptr'] = ptr

    # Loads in all relevant templates. Should find a more scalable way to do this.
    env = Environment(loader=FileSystemLoader('templates/'))
    zone_template = env.get_template('home.arpa.zone.j2')
    reverse_template = env.get_template('db.192.168.j2')
    bind9_conf_template = env.get_template('named.conf.j2')

    # Renders all templates with the datafile.
    zone_conf = zone_template.render(data)
    reverse_conf = reverse_template.render(data)
    bind9_conf = bind9_conf_template.render(data)

    # Write all outputs into discrete files.
    try:

        # Writing github artifacts
        with open('../artifacts/home.arpa.zone', 'w') as file:
            file.write(zone_conf)
        
        with open('../artifacts/db.192.168', 'w') as file:
            file.write(reverse_conf)

        with open('../artifacts/named.conf', 'w') as file:
            file.write(bind9_conf)

    except Exception as e:
        print(f"EXCEPTION: \n\n{e}")

if __name__ == '__main__':
    main()