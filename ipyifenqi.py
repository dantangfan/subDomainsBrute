import nmap
from ports import ports
import json


p = []
for k, v in ports.iteritems():
    p.append(str(v))

p = ','.join(p)

ips = [
"120.26.219.144",
"162.213.208.2",
"162.213.208.2",
"120.26.219.144",
"220.181.72.229",
"115.29.246.28" ]

#p='21,22'
#ips=['127.0.0.1']

answer = []
for ip in ips:
    nm = nmap.PortScanner()
    res = nm.scan(ip, p)
    scan = res['scan']
    for k, v in scan.iteritems():
        tcp = v['tcp']
        for kk, vv in tcp.iteritems():
            if vv['state'] == 'open':
                answer.append(str(k) + ':' + str(kk))

for a in answer:
    print answer
