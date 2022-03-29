import os
import sys,time
from setup import colors
c = colors
def sprint(str):
	for i in str +c.c + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()

		time.sleep(3/90)


def command(str):
	os.system(str)