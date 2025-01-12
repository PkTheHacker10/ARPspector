from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    from modules.cli.cli import commandline
    from modules.handler import ArpSpectorHandler
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] [arpspector] Import Error :{reset} {ie}")
    exit(1)
    
def main():
    # Main function to start ARPspector.``
    print(commandline.banner())
    arpspector_main_handler=ArpSpectorHandler()
    arpspector_main_handler.handler()

if __name__=="__main__":
    main()
