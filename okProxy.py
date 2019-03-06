import requests
import json
import random
from halo import Halo

spinner = Halo(text='Wait Wait , just wait and watch', spinner='dots',color='green')

def get_proxies():
    proxies = []
    f = open("proxy-list.txt", "r", encoding = "ISO-8859-1")

    for line in f.readlines():
        v = line.split(" ")
        proxies.append(v[0])
    return proxies

proxies = get_proxies()

okProxies = []

spinner.start()
for proxy in proxies:
    try:
        r = requests.get('http://ip.42.pl/raw',proxies={'http': proxy}).text
        spinner.succeed(proxy+" a good IP")
        okProxies.append(proxy)        
    except:
        spinner.fail(proxy+" a very bad IP")

print(okProxies)