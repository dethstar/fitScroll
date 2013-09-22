from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
import time
#4 mueve hacia arriba
#5 mueve hacia abajo
def girale(mov):
	d = Display()
	m = 4 if mov==1 else 5
	fake_input(d,X.ButtonPress,m)
	d.sync()
	fake_input(d,X.ButtonRelease,m)
	d.sync()



