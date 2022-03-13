import os
import platform

from codes.colors import ran , y , g , w , r , c
import colors

try:
    from colorama import Fore, Back

except ModuleNotFoundError:
    os.system("pip instll colorama")

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
 ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  {w}<{y}/{w}> {GB}{w}Instagram : @saadkhan041 {Back.RESET}
▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    {w}<{y}/{w}> {YB}{w}Instagram : @coding_memz {Back.RESET}
▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  {w}<{y}/{w}> {WB}{w}Github: Saadkhan041 {Back.RESET}
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
  ███    ███                                      ███    ███ 
  
                                    {y}<{w}/{y}> {c}Author: {w}Saad Khan 
  """
# logo = f"""
# ██╗██████╗
# ██║██╔══██╗
# ██║██████╔╝
# ██║██╔═══╝
# ██║██║
# ╚═╝╚═╝
#
# ██████╗  ██████╗ ██╗   ██╗███████╗██████╗
# ██╔══██╗██╔═══██╗██║   ██║██╔════╝██╔══██╗
# ██████╔╝██║   ██║██║   ██║█████╗  ██████╔╝
# ██╔══██╗██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
# ██║  ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
# ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
#
# """
from colorama import Fore,Style
c = colors
def banner():
    print(c.ran + logo)


def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "\n", "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def clear():
    os.system("cls") if  "Windows" in platform.platform() else os.system("clear")