import sys
import logging
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    from cli.cli import commandline
    from inspector.monitor import ArpInspector
    from threading import Thread
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] Import Error :{reset} {ie}")

class ArpSpectorHandler():
    def __init__(self):
        self.inspector=ArpInspector()
        self.arguments=commandline.argment_parser()
                
    def handler(self):
        
        if self.arguments.help:
            _help=commandline.help()
            print(_help)
            exit()
        
        if self.arguments.interface is not None:
            print("Inspector on duty...")
            inspector_handler_thread=Thread(target=self.inspector.inspector_handler(),args=())
            #sniffer_thread.start()
            #sniffer_thread=Thread(target=self.inspector.sniffer(),args=())
            inspector_handler_thread.start()
                
        else:
            print(f"{bright}{red} [ ERROR ]{reset}: Missing required argumets.")
            print(f" {bright}{blue} Usage :{sys.argv[0]} {reset}-i {red}<interface>{reset} [options]\n {blue} Use --help for more information.{reset}\n")
            exit(1)

            
if __name__=="__main__":
    spector=ArpSpectorHandler()
    spector.handler()