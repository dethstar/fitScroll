from Xlib import X
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
import time
#4 mueve hacia arriba
#5 mueve hacia abajo
def girale(d):
	fake_input(d,X.ButtonPress,5)
	d.sync()
	fake_input(d,X.ButtonRelease,5)
	d.sync()

d = Display()
time.sleep(4)
print "girando"
girale(d)
print "giro"

