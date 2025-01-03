import sys
import argparse
import requests
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
white=Fore.WHITE
magenta=Fore.MAGENTA
bright=Style.BRIGHT
green=Fore.GREEN
red=Fore.RED
bold=Style.BRIGHT
reset=Style.RESET_ALL

class commandline():
    
    def argment_parser():
    #function to get arguments.
        parser=argparse.ArgumentParser(add_help=False,usage=argparse.SUPPRESS,exit_on_error=False)
        try:
            parser.add_argument("-i","--interface",type=str)
            parser.add_argument("-l","--log",type=str,default="/tmp/arpspector.log")
            args=parser.parse_args()
            return args
        
        except argparse.ArgumentError:
            print(f"{bright}{red}\n [+] {reset}{blue}Please use -h to get more information.")
            
        except argparse.ArgumentTypeError:
            print(f"{bright}{blue}\n [+] {reset}{blue}Please use -h to get more information.")
            
        except Exception as e:
            print(f"{bright}{red}\n [+] {reset}{blue}Unexpected Argument Error:{e}")
            
def help():
    # Funtion to create and return the available options and flags.
    return f"""\n
{bold}{white}[{reset}{bold}{blue}DESCRIPTION{reset}{white}]{reset}: {white}{bold}ARPspector{reset} {white}is a tool by {reset}{bold}{green}PkTheHacker10{reset}.Which is used to detect ARP spoofing in the network.\n
    {bold}{white}[{reset}{bold}{blue}Usage{reset}{white}]{reset}:{sys.argv[0]} -i <interface> [-l logfile]\n
            {white}phonyARP {bold}{white}[{reset}{bold}{blue}flags{reset}{bold}{white}]\n
    [{reset}{bold}{blue}flags{reset}{bold}{white}]
                
            [{reset}{bold}{blue}input{reset}{bold}{white}]{reset}
            
                -i,   --interface               :  Interface is used to moniter the network [mandatory]  
                    
            {bold}{white}[{reset}{bold}{blue}debug{reset}{bold}{white}]{reset}
                -l,   --log                     :  To save the network log in a file [default : /tmp/arpspector.log] 
                -v,   --version                 :  To check version of this tool. 
                -h,   --help                    :  To see all the available options.
          """
def get_version():
    #funtion which is used to get the version (tag) from github through api.
    # TODO remove else after tool become public.
    try:
        url="https://api.github.com/repos/PkTheHacker10/ARPspector/releases/latest"
        response=requests.get(url,timeout=3,verify=True)
        if response.status_code==200:
            json_data=response.json()
            latest=json_data.get('tag_name')
            return latest
        else:
            return "v1.0.0"
        
    except (requests.ConnectTimeout,requests.ReadTimeout,requests.Timeout):
        print(f"{bright}{blue}\n [+] {reset} : Connection TimeOut while getting version.")
        
    except requests.JSONDecodeError:
        print(f"{bright}{red}\n [+] {reset} : Couldn't decode data.")
        
