import os 
from colorama import Fore,Style 

red=Fore.RED
blue=Fore.BLUE
bright=Style.BRIGHT
white=Fore.WHITE
reset=Style.RESET_ALL

class fileoperation():
    # File operation class.
    def writefile(self,file,mode,data):
    #Function to write the data in the file.
        try:
            if os.path.isfile(file):
                with open(file,mode) as write_file:
                    overwrite_decision=input(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: File \"{file}\" Already exist, Do you want to overwrite (Y)es or (N)o:").lower()
                    
                    if overwrite_decision == "y":
                        write_file.write(data)
                        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: File \"{file}\" Overwrited succesfully.")
                        
                    elif overwrite_decision == "n":
                        write_file.write(data)
                        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Saved in default location \"{file}\" succesfully.")
                        
                    else:
                        print(f"{bright}{white}[{reset}{red}ERROR{reset}{bright}{white}]{reset}: Invalid option.")
                        write_file.write(data)
                        print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: Saved in default location \"{file}\" succesfully.")      
                        
            else:
                with open(file,mode) as write_file:
                    write_file.write(data)
                    print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}:File saved as \"{file}\" succesfully.")    
                    
        except PermissionError:
            print(f"{bright}{white}[{reset}{blue}INFO{reset}{bright}{white}]{reset}: File \"{file}\" don't have permission to read.")
