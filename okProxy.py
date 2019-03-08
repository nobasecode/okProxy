# NoBaseCode - Mohamed LAABID
# Note: you need to install both halo and progress packages , or you can get rid of them in the code


import requests
import json
import random
from halo import Halo
from progress.bar import Bar

spinner = Halo(text='Give it time', spinner='dots',color='green')

def get_proxies():
    proxies = []
    f = open("proxy-list.txt", "r", encoding = "ISO-8859-1")

    for line in f.readlines():
        v = line.split(" ")
        proxies.append(v[0])
    return proxies

proxies = get_proxies()
bar = Bar('Processing', max=len(proxies))

okProxies = []

spinner.start()
for proxy in proxies:
    bar.next()
    try:
        r = requests.get('http://ip.42.pl/raw',proxies={'http': proxy}).text
        spinner.succeed(proxy+" work fine")
        okProxies.append(proxy)        
    except:
        spinner.fail(proxy+" a bad IP")

bar.finish()
with open('valideProxies.txt', 'w') as f:
    f.write("\n".join(okProxies))