import argparse
from pyhunter import PyHunter

parser = argparse.ArgumentParser(description="Hunter.io Bulk Email Search With API Key")
parser.add_argument('--key', '-k', help='Hunter.io API Key', required=True)
parser.add_argument('--domain', '-d', help='Domain that will be searched.',required=True)
parse = parser.parse_args()

def hunter(key, domain):
    hunter = PyHunter(key)
    out = hunter.domain_search(domain)
    mails = [i["value"] for i in out["emails"]]
    return mails

def main():
    output = hunter(parse.key, parse.domain)
    print(*output, sep=("\n"))

main()