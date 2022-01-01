import ipapi
from codes import colors
from codes.banner import logo , clear

c = colors
from colorama import Fore,Style

clear()

def banner():
    print(c.ran + logo)
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "\n", "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

banner()
def banner2():
    print(c.ran + '-'*63)
    print("|" + "*"* 60 + c.ran + "|")

    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4 + c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4+c.ran + "|")
    print(c.ran + "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3+c.ran + "|")
    print(c.ran + "|"+ "\n", "*" * 60+c.ran + "|")

    print(c.ran + '-' * 63)

def program():

    ip = input(c.ran + "Enter target ip: " +c.ran)
    location = ipapi.location(ip)

    for k , v in location.items():
        print(c.c + k + " : " + c.lr + str(v))

yes = ['y' , 'yes']
no = ['n' , 'no']

cont = ""
while cont not in no:
    program()
    cont = input(c.lg + "Do you want to continue? [y/n]")
    if cont in no:
        banner2()
    else:
        clear()
        banner2()
