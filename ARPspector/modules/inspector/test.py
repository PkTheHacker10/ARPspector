from scapy.all import *

while True:
    ether_frame=Ether(dst="ff:ff:ff:ff:ff:ff")
    arp=ARP(pdst="192.168.53.156")
    packet=ether_frame/arp
    ans=sendp(packet)