from time import sleep
from scapy.all import *
from threading import Thread,ThreadError,Lock
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

arp_packet=[]
lock=Lock()
class ArpInspector():
    
    def logger(self):
        pass
    
    def packet_analyzer(self,packet):
        if ARP in packet:
            if packet[ARP].op == 2: 
                print(f" [Reply] : i {packet[ARP].psrc} has {packet[ARP].hwsrc} asking to {packet[ARP].pdst} to store my MAC")
            
    def inspector_handler(self):
        try:
            packet=sniff(filter="arp",prn=self.packet_analyzer,store=False)
            
            
        except ThreadError as ThreadingError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {ThreadingError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.inspector_handler()
    