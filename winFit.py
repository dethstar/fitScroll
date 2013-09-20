import time, win32api
from win32con import *

def girale(x,y):
	time.sleep(2)
	win32api.mouse_event(0x0800,x,y,120,0)

x,y = win32api.GetCursorPos()
girale(x,y)

# mouse move 'MOVE'        : 0x0001, 
# Left button down 'LEFTDOWN'    : 0x0002, 
# Left button up  'LEFTUP'      : 0x0004, 
# Right button down  'RIGHTDOWN'   : 0x0008,
# Right button up  'RIGHTUP'     : 0x0010,
# middle button down  'MIDDLEDOWN'  : 0x0020, 
# middle button up  'MIDDLEUP'    : 0x0040, 
# x button down  'XDOWN'       : 0x0080, 
# x button down  'XUP'         : 0x0100, 
# wheel button rolled  'WHEEL'       : 0x0800, 
# map To entire virtual Desktop  'VIRTUALDESK' : 0x4000, 
# absolute move   'ABSOLUTE'    : 0x8000, 