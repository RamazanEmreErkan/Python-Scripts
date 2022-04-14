import ipaddress
import json
import argparse
import time
import shodan

parser = argparse.ArgumentParser(description="Gets an IP block and return ports of IP addresses from Shodan.")
requiredNamed = parser.add_argument_group('required  arguments')
requiredNamed.add_argument('--inputfile', '-f', help='File that contains CIDR IP Blocks.', required=True)
requiredNamed.add_argument('--key', '-k', help='Shodan API key.', required=True)

parser.add_argument('--delay', '-d', default=0, help='Delay second for API Query Limit.', type=float)
parser.add_argument('--output', '-o', default="out.json", help='Output filename. json format recommended.')
parser.add_argument('--allscan', '-a', help='Get all response from Shodan instead of getting only port information.')
parse = parser.parse_args()

class CIDR:
    def __init__(self):
        self.ip_list = list()
        self.input = parse.inputfile
        self.cidr_to_ip()
    
    def cidr_to_ip(self):
        with open(self.input, "r") as fp: 
            blocks = fp.readlines()

        for block in blocks:
            try:
                self.ip_list.extend([str(ip) for ip in ipaddress.IPv4Network(block.rstrip(), False)])
            except ipaddress.AddressValueError as e:
                print(e)

    def get_list(self):
        return self.ip_list
    # # Use this method if only check ip list externally. 
    # def export_ip_list(self):
    #     with open("ip_list_export.txt", "w") as fp:
    #         for i in self.ip_list:
    #             fp.write(i)
    #             fp.write("\n")


class Shodan:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api = shodan.Shodan(self.api_key)
        cidr_obj = CIDR()
        self.ip_list = cidr_obj.get_list()
        self.shodan_get_results()

    def shodan_get_results(self):
        ipInfo = dict()
        portInfo = dict()

        for ip in self.ip_list:
            try:
                print(f'[INFO] - fetching host {ip}')
                hostInfo = self.api.host(ip)
                if parse.allscan:                    
                    ipInfo[ip] = hostInfo
                    time.sleep(parse.delay)
                else:
                    portInfo[ip] = hostInfo["ports"]
                    time.sleep(parse.delay)
            except shodan.APIError as e:
                print(e)
                time.sleep(parse.delay)

        if parse.allscan:
            self.output(ipInfo)
        else:
            self.output(portInfo)

    def output(self, write_file):
        with open(parse.output, "w") as fp:
            fp.write(json.dumps(write_file))
        print(f'[INFO] Output written to {parse.output}')     

def main():    
    Shodan(parse.key)

main()