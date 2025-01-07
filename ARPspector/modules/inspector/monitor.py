from time import sleep
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import sendp
from scapy.all import sniff
from threading import Thread,Lock
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
            print("Sniffer started")
            global arp_packet
            sniffer_thread=Thread(target=self.sniffer,args=())
            sniffer_thread.start()
            sleep(1)
            i=1
            while True:
                with lock:
                    packet_count=len(arp_packet)
                    if arp_packet:
                        print(f"arp pack exist and Length {packet_count}")
                        # print(f"Packet count: {len(arp_packet)}")
                        # for arp in arp_packet.values():
                        #     print(f"Request {i} :{arp}")
                        #     print("------------------------------------------------------------------------")
                        # i=i+1
                    else:
                        continue

            
        except Exception as InspectorHandlerError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {InspectorHandlerError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.inspector_handler()
    