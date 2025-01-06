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
                global arp_packet
                packet=sniff(filter="arp",count=1)
                arp=packet[0]
                if ARP in arp:
                    arp_packet["arp_replay"]={
                        "src_ip":arp.psrc,
                        "src_mac":arp.hwdst,
                        "dst_ip":arp.pdst,
                        "dst_mac":arp.hwdst
                        }
                print(arp_packet)
                   
        except Exception as SnifferError:
            print(f"{bright}{red}[ + ] Error on sniffer: {SnifferError}{reset}")
            
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
    