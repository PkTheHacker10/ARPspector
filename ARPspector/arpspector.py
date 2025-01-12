from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
green=Fore.GREEN
reset=Style.RESET_ALL

try:
    from ARPspector.modules.cli.cli import commandline
    from ARPspector.modules.handler import ArpSpectorHandler
    
except ImportError as ie:
    print(f" {bright}{red}[ + ] [arpspector] Import Error :{reset} {ie}")
    exit(1)
    
def main():
    # Main function to start ARPspector.
    cli=commandline()
    print(commandline.banner())
    print(f"\n\t ARPspector {green}{cli.get_version()}{reset} is a tool by PkTheHacker10.\n")
    arpspector_main_handler=ArpSpectorHandler()
    arpspector_main_handler.handler()
