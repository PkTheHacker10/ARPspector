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

class ArpInspector():
    
    def sniffer(self):
        while True:
            try:
                Lock.acquire()
                arp_packet.append(sniff(filter="arp")[0])
                
            except Exception as LockError:
                print(f" {bright}{red}[ + ] Sniffing Error :{reset} {LockError}")
                
            finally:
                Lock.release()
            
    
    def logger(self):
        pass
    
    def inspector_handler(self):
        try:
            sniffer_thread=Thread(target=self.sniffer(),args=())
            sniffer_thread.start()
            
        except ThreadError as ThreadingError:
            print(f" {bright}{red}[ + ] Thread Error :{reset} {ThreadingError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.sniffer()
    