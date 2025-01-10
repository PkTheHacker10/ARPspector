from platform import system
from time import sleep
from scapy.layers.l2 import ARP
from scapy.all import sniff
from threading import Thread,Lock
from re import findall
from subprocess import run
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

arp_packet=dict()
lock=Lock()
    
class ArpInspector():
    
    def sniffer(self):
        try:
            global arp_packet
            print("Sniffer started")
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
            
    def arp_table_inspector(self):
        
        print("Table inspector started")
        flag=""
        if system().lower() == "windows":
            flag="-a"
        elif system().lower() == "linux":
            flag="-n"
        try:
            spoofed_ip_mac=dict()
            while True:
                sleep(3)
                result=run(["arp",flag],capture_output=True,text=True)
                arp_table=result.stdout
                all_ip=findall(r"((?:\d{1,3}\.){3}\d{1,3})",arp_table)
                all_mac=findall(r"([0-9a-fA-Z]{2}:[0-9a-fA-Z]{2}:[0-9a-fA-Z]{2}:[0-9a-fA-Z]{2}:[0-9a-fA-Z]{2}:[0-9a-fA-Z]{2})",arp_table)
                # ip and mac regex
                ip_mac=dict(zip(all_ip,all_mac))
                for ip,mac in ip_mac.items():
                    if all_mac.count(mac) > 1:
                        for host in range(1,all_mac.count(mac)):
                            spoofed_ip_mac[ip]=mac
                if spoofed_ip_mac:
                    return spoofed_ip_mac
                    
        except Exception as ArpTableInspectorError:
            print(f"{bright}{red}[ + ] Error on arp table inspector: {ArpTableInspectorError}{reset}")
            
    def inspector_handler(self):
        try:
            global arp_packet
            i=1
            while True:
                sleep(1)
                with lock:
                    if arp_packet:
                        packet_count=len(arp_packet)
                        print(f"Total Packet count: {packet_count}")
                        try:
                            # Alert if the request sip ,smac make 10 request simultaniously to the same dst ip& mac.
                            print(f"Packet number :{i}")
                            for key,data in arp_packet[f"arp_replay: {i}"].items():
                                print(f"{key} :{data}")
                                
                            del arp_packet[f"arp_replay: {i}"]
                            print(f"arp_packet [arp_replay: {i}] deleted...")
                            
                            print("------------------------------------------------------------------------")
                        except Exception as e:
                            print(f"Delete error: {e}")
                    else:
                        continue

            
        except Exception as InspectorHandlerError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {InspectorHandlerError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.arp_table_inspector()
    