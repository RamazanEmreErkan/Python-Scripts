import socket
import sys
import argparse
import ipaddress
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-v","--title", help= "title information of HTTP page.", action="store_true")
parser.add_argument("-i", "--target", help= "ip range that will be scanned. Example:'-i 192.168.1.0-192.168.1.255'", action="store")
args = parser.parse_args()

#-i = '192.168.1.0-192.168.1.4'

def Main():
    if args.target:
        splitter(args.target)

def scrap(var): 
    url = 'http://'+var # prepare the ip address to scraping
    r = requests.get(url)
    html = BeautifulSoup(r.text,"html.parser") #scraping
    if(html == ""):
        print("\t"+url+" has no title"+"\n")
    else:
        print(url+" 's title:"+ "-"*5+">"+html.title.text+"\n")


def splitter(ip): #split to 2 parts the ip range that came from console 
    ips = []
    ips = ip.split('-')
    startIp = ips[0]
    endIp = ips[1]
    ranger(startIp , endIp)

def ranger(val1 , val2):
    section1 = []
    section2 = []
    section1 = val1.split('.')
    section2 = val2.split('.')

    rangeVal1 = int(section1[3])
    rangeVal2 = int(section2[3])

    section1.pop(-1) #combine starting ip without last cell
    rootIp = '.'.join(section1) 
    scanner(rangeVal1, rangeVal2, rootIp)


def scanner(rval1 , rval2, rIp):

    for i in range(rval1, rval2+1):
        host = rIp +"."+str(i) #create ip address in given range
        port = 80

        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            con = sc.connect((host,port))
            print(host+"'s http port is open")
            if args.title: # if block runs when title argument is written in console
                scrap(host)
                sc.close()
        except Exception:
            pass

if __name__ == '__main__':
    Main()
