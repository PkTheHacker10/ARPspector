import logging
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    from ARPspector.modules.cli.cli import commandline
    from ARPspector.modules.inspector.monitor import ArpInspector
    from threading import Thread,Event
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] [handler] Import Error :{reset} {ie}")


class ArpSpectorHandler():
    # Class to handle ARPspector.
    def __init__(self):
        self.stop_event=Event()
        self.inspector=ArpInspector()
        self.arguments=commandline.argment_parser()
                
    def handler(self):
        # Function to handle ARPspector.
        if self.arguments.help:
            _help=commandline.help()
            print(_help)
            exit()
        
        if self.arguments.log_file != "../log/arpspector.log":
            print(f"{bright}{blue}[ + ]{reset}{white} Log file is set :{self.arguments.log_file}")
        
        try:
            print(f"{bright}{blue}[ + ]{reset}{white} ARPspector started.{reset}")
            print(f"{bright}{blue}[ + ]{reset}{white} Press Ctrl+C to stop.{reset}")
            logging.basicConfig(filename=self.arguments.log_file,level=logging.WARNING)
            table_inspector=Thread(target=self.inspector.arp_table_inspector)
            table_inspector.start()
            table_inspector.join()
        
        except KeyboardInterrupt:
            print(f"{bright}{red}\n[ + ]{reset}{white} ARPspector stopped.{reset}")
            self.stop_event.set()
            table_inspector.join()
            exit()

            
if __name__=="__main__":
    spector=ArpSpectorHandler()
    spector.handler()