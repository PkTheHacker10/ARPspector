from subprocess import run
from os import system

user_name=run(["whoami"],capture_output=True,text=True)
system("mkdir /home/"+user_name.stdout.strip()+"/arpspector")
LOG_FILE="/home/"+user_name.stdout.strip()+"arpspector"+"/ARPspector.log"