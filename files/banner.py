import os
from files.colors import r , g , w , c , y

from files.colors import r , g , w , c , y , ran
try:
    from colorama import Back , Fore , Style

except ModuleNotFoundError:
    os.system("pip install colorama")

GB = Back.GREEN
YB = Back.YELLOW
WB = Back.RED 


logo = f"""
 ▄█     █▄   ▄█  ███▄▄▄▄   ████████▄   ▄██████▄   ▄█     █▄     ▄████████ 
███     ███ ███  ███▀▀▀██▄ ███   ▀███ ███    ███ ███     ███   ███    ███ 
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███    █▀  
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███   ███        
███     ███ ███▌ ███   ███ ███    ███ ███    ███ ███     ███ ▀███████████ 
███     ███ ███  ███   ███ ███    ███ ███    ███ ███     ███          ███ 
███ ▄█▄ ███ ███  ███   ███ ███   ▄███ ███    ███ ███ ▄█▄ ███    ▄█    ███ 
 ▀███▀███▀  █▀    ▀█   █▀  ████████▀   ▀██████▀   ▀███▀███▀   ▄████████▀  
                                                                          
    ███        ▄████████  ▄██████▄       ▄█    ▄████████ ███▄▄▄▄          
▀█████████▄   ███    ███ ███    ███     ███   ███    ███ ███▀▀▀██▄        
   ▀███▀▀██   ███    ███ ███    ███     ███   ███    ███ ███   ███        
    ███   ▀  ▄███▄▄▄▄██▀ ███    ███     ███   ███    ███ ███   ███        
    ███     ▀▀███▀▀▀▀▀   ███    ███     ███ ▀███████████ ███   ███        
    ███     ▀███████████ ███    ███     ███   ███    ███ ███   ███        
    ███       ███    ███ ███    ███     ███   ███    ███ ███   ███        
   ▄████▀     ███    ███  ▀██████▀  █▄ ▄███   ███    █▀   ▀█   █▀         
              ███    ███            ▀▀▀▀▀▀                                                                 
"""

lololo = f"""
 ▄█     ▄███████▄                                            
███    ███    ███                                            
███▌   ███    ███                                            
███▌   ███    ███                                            
███▌ ▀█████████▀                                             
███    ███                                                   
███    ███                                                   
█▀    ▄████▀                                                 
                                                             
   ▄████████  ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███ ███    ███ ███    ███   ███    █▀    ███    ███ 
 ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  {w}<{y}/{w}> {GB}{w}Instagram : @saadkhan041 {Back.RESET}
▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    {w}<{y}/{w}> {YB}{w}Instagram : @coding_memz {Back.RESET}
▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  {w}<{y}/{w}> {WB}{w}Github: Saadkhan041 {Back.RESET}
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
  ███    ███                                      ███    ███ 
                                    
                                    {y}<{w}/{y}> {c}Author: {w}Saad Khan     
"""
from files.colors import *


def banner():
    print(ran + lololo)


def banner2():

    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX,  "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+ran + "|")
    print(ran + "\n","|"+ Style.BRIGHT + Fore.LIGHTRED_EX,  "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+ran + "|")

def clear():
    os.system("clear")


