import ipapi
from setup.banner import banner , banner2 , clear
from files import colors


c = colors

clear()

banner()


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
        clear()
        banner2()
    else:
        clear()
        banner2()
