from time import sleep
from scapy.all import *
from threading import Thread,ThreadError,Lock
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

arp_packet=dict()
lock=Lock()
class ArpInspector():
    
    def logger(self):
        pass
    
    def sniffer(self):
        try:
            print("inside sniffer")
            while True:
                packet=sniff(filter="arp",count=1)
                if ARP in packet[0]:
                    if packet[ARP].show().op == 2:
                        arp_packet["arp_replay"]={
                            "src_ip":packet[ARP].psrc,
                            "src_mac":packet[ARP].hwdst,
                            "dst_ip":packet[ARP].pdst,
                            "dst_mac":packet[ARP].hwdst
                        }
                    
        except Exception as SnifferError:
            print(f"{bright}{red}[ + ] Error on sniffer: {SnifferError}")
            
    def inspector_handler(self):
        try:
            sniffer_thread=Thread(target=self.sniffer,args=())
            sniffer_thread.start()
            
            for i in range(1,10):
                print(arp_packet)
                print("sleeping 2 sec..")
                sleep(2)
            
        except Exception as InspectorHandlerError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {InspectorHandlerError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.inspector_handler()
    