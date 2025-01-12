from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    import logging
    from platform import system
    from time import sleep
    from threading import Thread,Event
    from re import findall
    from subprocess import run
    from modules.cli.cli import commandline
    
except ImportError as Importerror:
    print(f" {bright}{red}[ + ] [monitor] Import Error :{reset} {Importerror}")
    exit(1)
    
stop_event=Event()
    
class ArpInspector():
    # Class to handle ARP table inspection.
    def __init__(self):
        self.arguments=commandline.argment_parser()
        try:
            logging.basicConfig(filename=self.arguments.log_file,format='%(asctime)s %(message)s',filemode="a")
            logger=logging.getLogger()
            logger.setLevel(logging.DEBUG)
            
        except Exception as LoggingError:
            print(f"{bright}{red}[ + ] Unexpected error on logging configuration: {reset}{LoggingError}")
            exit(1)
            
        logging.info("ARPspector started.")
            
    def arp_table_inspector(self):
        # Function to inspect ARP table.
        try:
            flag=""
            if system().lower() == "windows":
                flag="-a"
            elif system().lower() == "linux":
                flag="-n"

            spoofed_ip_mac=dict()
            logging_counter=1
            while not stop_event.is_set():
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
                    try:
                        for ip,mac in spoofed_ip_mac.items():
                            if logging_counter == 1:
                                logging.warning(f"Spoofing detected [{ip} : {mac}]")
                                print(f"{bright}{red}[ + ] Spoofing ip and mac detected :{reset} [ {ip} : {mac} ]")
                                
                            if logging_counter % 10 == 0:
                                logging.warning(f"Spoofing still running [{ip} : {mac}]")
                                print(f"{bright}{red}[ + ] Spoofing still running [{logging_counter}]:{reset} {ip} : {mac}")
                                
                            if self.arguments.verbose:
                                print(f"{bright}{red}[ + ] Spoofed ip and mac detected [{logging_counter}]:{reset} {ip} : {mac}")
                            
                    except Exception as ArpTableInspectorError:
                        print(f"{bright}{red}[ + ] Unexpectod error on arp table inspector.spoofed_ip_mac: {ArpTableInspectorError}{reset}")
                        stop_event.set()
                        exit(1)
                                
                    logging_counter=logging_counter+1
                    spoofed_ip_mac.clear()
                
        except Exception as ArpTableInspectorError:
            print(f"{bright}{red}[ + ] Unexpectod error on arp table inspector: {ArpTableInspectorError}{reset}")
            exit(1)
            
    def inspector_handler(self):
        # Function to handle ARP table inspection.
        try:
            arp_table_inspector_thread=Thread(target=self.arp_table_inspector,args=())
            arp_table_inspector_thread.start()
            
        except Exception as InspectorHandlerError:
            print(f" {bright}{red}[ + ] Unexpectod error on inspector Thread :{reset} {InspectorHandlerError}")
            
        
            
if __name__=="__main__":
    ai=ArpInspector()
    ai.arp_table_inspector()
    