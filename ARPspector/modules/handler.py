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
    from file.file import fileoperation
    from inspector.monitor import ArpInspector
    from threading import Thread
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] Import Error :{reset} {ie}")

class ArpSpectorHandler():
    def __init__(self):
        self.arguments=commandline.argment_parser()
        self.inspector=ArpInspector()
        
    def handler(self):
        try:
            logging.basicConfig(filename=self.arguments.log_file,format='%(asctime)s %(message)s',filemode="a")
            logger=logging.getLogger()
            logger.setLevel(logging.DEBUG)
    
        except Exception as e:
            print(f"Exception : {e}")
        
        if self.arguments.help:
            _help=commandline.help()
            print(_help)
            exit()
        
        if self.arguments.interface is not None:
            print("Inspector on duty...")
            #inspector_handler_thread=Thread(target=self.inspector.inspector_handler(),args=())
            #sniffer_thread.start()
            #sniffer_thread=Thread(target=self.inspector.sniffer(),args=())
            arp_table_inspector_thread=Thread(target=self.inspector.arp_table_inspector,args=())
            arp_table_inspector_thread.start()
            #inspector_handler_thread.start()
            
            
        else:
            print(f"{bright}{red} [ ERROR ]{reset}: Missing required argumets.")
            print(f" {bright}{blue} Usage :{sys.argv[0]} {reset}-i {red}<interface>{reset} [options]\n {blue} Use --help for more information.{reset}\n")
            exit(1)

            
if __name__=="__main__":
    spector=ArpSpectorHandler()
    spector.handler()