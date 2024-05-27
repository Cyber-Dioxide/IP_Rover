import os
import platform
from scripts import colors
from scripts.colors import r, g, y, c, w
from colorama import Fore, Back

GB = Back.GREEN
YB = Back.YELLOW
WB = Back.RED

logo = f"""
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
     ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  
    ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    
    ▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████ 
      ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
      ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
      ███    ███                                      ███    ███ 
      
                 </> Author: Cyber-Dioxide    
               </> Telegram : @cyberdioxide                                                                                                      
"""
c = colors
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")


def banner():
    print(c.ran + logo)


def banner2():
    print()


def clear():
    s = platform.platform()
    if "Windows" in s:
        os.system("cls")
    else:
        os.system("cls") if "Windows" in platform.platform() else os.system("clear")
