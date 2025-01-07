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
            print("sniffer started")
            global arp_packet
            i=1
            while True:
                packet=sniff(filter="arp",count=1)
                arp=packet[0]
                if ARP in arp:
                    with lock:
                        arp_packet[f"arp_replay: {i}"]={
                            "src_ip":arp.psrc,
                            "src_mac":arp.hwdst,
                            "dst_ip":arp.pdst,
                            "dst_mac":arp.hwdst
                            }
                    i=i+1
                   
        except Exception as SnifferError:
            print(f"{bright}{red}[ + ] Error on sniffer: {SnifferError}{reset}")
            
    def inspector_handler(self):
        try:
            global arp_packet
            sniffer_thread=Thread(target=self.sniffer,args=())
            sniffer_thread.start()
            while True:
                print(arp_packet)
                print(f"Length : {len(arp_packet)}")
                print("------------------------------------------")
                print("sleeping 0.6 sec..")
                sleep(0.6)
            
        except Exception as InspectorHandlerError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {InspectorHandlerError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.inspector_handler()
    