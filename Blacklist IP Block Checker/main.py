"""
Name : Blacklist IP Block Checker
Definition: IP Blocks can be controlled via Blacklists.
Author : Ramazan Emre Erkan
Usage : Just run the file.
Compatibility: Python3.0+
"""
import ipaddress
import requests
from time import time

def daily_blacklist():
    # curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1
    r = requests.get("https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt")
    raw_blacklist = r.text.split("\n")
    return [ip for ip in raw_blacklist if not ip.startswith("#")]

RAWBLACKLIST = daily_blacklist()

class BlacklistChecker:
    def __init__(self):        
        self.ip_list = list()
        
    def ip_lister(self, input):
        with open("Inputs/"+input, "r") as fp: 
            blocks = fp.readlines()
        for block in blocks:
            if block == "\n" or block.startswith("#"):
                continue
            else:
                try:
                    self.ip_list.extend([str(ip) for ip in ipaddress.IPv4Network(block.rstrip(), False)])
                except ipaddress.AddressValueError as e:
                    print(e)
                    
    def intersection1(self):
        # Incredibly slow but shows ip-seencount
        matched_ip_lst = [value for value in RAWBLACKLIST if value.split("\t")[0] in self.ip_list]
        print(*matched_ip_lst, sep="\n")
        return matched_ip_lst

    def intersection2(self):
        # Uses set().intersection
        # Faster but shows only matched IP.
        cleaned_blacklist = [i.split("\t")[0] for i in RAWBLACKLIST]
        matched_ip_lst = set(self.ip_list).intersection(cleaned_blacklist)
        return matched_ip_lst

def main(inp): 
    obj = BlacklistChecker()
    obj.ip_lister(inp)
    output = obj.intersection2()
    if output:
        print("\nMatched IP adresses and counts of Blacklists they've been seen:\n")
        print(*output, sep="\n")
    else:
        print("No valid matches")

# For Testing
def measure_elapsed_time(inp, test_count):
    print('Testing process. Please wait until finish.')
    obj = BlacklistChecker()
    obj.ip_lister(inp)

    elapsed = 0
    for i in range(test_count):
        t1 = time()
        obj.intersection1()
        t2 = time()
        elapsed += (t2-t1)
        print("\t{}. try -> {:.2f}".format(i, t2-t1))
    average_time1 = elapsed/test_count
    print("Measured average elapsed time of first intersection method: ", average_time1)

    elapsed2 = 0
    for i in range(test_count):
        t3 = time()
        obj.intersection2()
        t4 = time()
        elapsed2 += (t4-t3)
        print("\t{}. try -> {:.2f}".format(i, t4-t3))
    average_time2 = elapsed2/test_count
    print("Measured average elapsed time of second intersection method: ", average_time2)
    print("\nPercentage gap in response time: {:.0f} times faster/slower.".format(average_time1/average_time2))

if __name__ == "__main__":    
    inp = input("Please enter a input file name from /Inputs: ")
    main(inp)
    # measure_elapsed_time(inp=inp, test_count=1)
