#!/usr/bin/python

import sys
from scapy.all import ARP,send
a=ARP()
a.hwsrc="aa:aa:aa:aa:aa:aa"
#a.psrc="192.168.1.93"
#a.hwdst="d4:be:d9:dc:4c:20"
#a.pdst="192.168.1.12"
#a.hwdst="00:00:00:00:00:00"
#a.pdst="0.0.0.0"
a.psrc="0.0.0.0"
a.hwdst="ff:ff:ff:ff:ff:ff"
a.pdst="255.255.255.255"
send(a)

