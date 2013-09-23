import platform
import sys
if platform.system()=="Linux":
	device="/dev/tty"+sys.argv[1] #reads from command line
	import linFit
	scroll = linFit
elif platform.system()=="Windows":
	import winFit
	scroll = winFit
	device="COM3"
else:
	print("not supported")
	sys.exit(0)

del sys
del platform
#import serial
#import time
#serial = serial.Serial(device,9600)
while True:
	x=input()#serial.read()
	if x=="1":
#		time.sleep(2)
		scroll.girale(1)
	elif x=="-1":
#		time.sleep(2)
		scroll.girale(-1)
	else:
		print(x)
