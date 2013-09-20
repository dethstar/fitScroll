import time, win32api
from win32con import *

def girale(x,y):
	time.sleep(2)
	win32api.mouse_event(0x0800,x,y,120,0)

x,y = win32api.GetCursorPos()
girale(x,y)

