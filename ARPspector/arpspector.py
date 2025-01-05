from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

try:
    from modules.handler import ArpSpectorHandler
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] Import Error :{reset} {ie}")
    exit(1)
    
def main():
    arpspector_main_handler=ArpSpectorHandler()
    arpspector_main_handler.handler()

