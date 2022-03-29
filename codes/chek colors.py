import os
try:
    from colorama import Fore, Back

except ModuleNotFoundError:
    os.system("pip instll colorama")


from colors import w , ran , y , c 
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
 ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  </> Instagram : @saadkhan041 
▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    </> Instagram : @coding_memz 
▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  </> Github: Saadkhan041 
  ███    ███ ███    ███ ███    ███   ███    ███   ███    ███ 
  ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███ 
  ███    ███                                      ███    ███ 
  
                                    </>Author:Saad Khan 
  """

from random import choice


for i in logo:
    col = choice([Fore.RED , Fore.GREEN , Fore.CYAN , Fore.LIGHTWHITE_EX , Fore.MAGENTA , Fore.BLUE])

    print(col + i , end="")
