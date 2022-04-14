# Shodan IP Block Port Scanner
**Author : Ramazan Emre Erkan** 
**April 2022**

Shodan IP Block Port Scanner is a Shodan Api tool that takes IP blocks as an input and find open ports of IP Adresses that in IP blocks. If requested, it will fetch the entire scan instead of just finding the port.

## On Start 
```
$ cd "Shodan IP Block Port Scanner"
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 shodan_bulk_ip.py -f inputfile.txt -o output.json -k {Shodan_API_Key}
```

See project on [Source].

[Source]: <https://github.com/RamazanEmreErkan/Python-Scripts>
