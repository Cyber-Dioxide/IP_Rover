import ipapi
from scripts.banner import banner , banner2 , clear, logo
from files import colors
from rgbprint import Color, gradient_print

C1 = Color.magenta
C2 = Color.hot_pink

c = colors

clear()

gradient_print(logo, start_color=C1, end_color=C2)


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
