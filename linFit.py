from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input

def girale(mov):
	up=4 #4 scrolls up 
	down=5 #5 scrolls down 
	d = Display()
	m = up if mov==1 else down
	fake_input(d,X.ButtonPress,m)
	d.sync()
	fake_input(d,X.ButtonRelease,m)
	d.sync()



