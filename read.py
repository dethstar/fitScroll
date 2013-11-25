import platform
if platform.system()=="Linux":
	print "Leenux"
	import sys
	device="/dev/tty"+sys.argv[1] #reads from command line
	del sys
	import linFit
	scroll = linFit
elif platform.system()=="Windows":
	import winFit
	scroll = winFit
	device="COM3"
else:
	print("not supported")
	sys.exit(0)

del platform
import serial
serial = serial.Serial(device,9600)
while True:
	x=serial.read()#raw_input() 
	if x=="1":
	#	time.sleep(2)
		scroll.girale(1)
		print "arriba"
	elif x=="2":
		print 'abajo'
	#	time.sleep(2)
		scroll.girale(-1)
	else:
		print x
	x=0 