from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse

time.sleep(0.05)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while 1:
    if pyautogui.locateOnScreen ('leave.png', confidence=0.8) != None:
        mouse.move(1850,999, absolute=False, duration=0.2)
        mouse.click('left')
        mouse.move(-1822,-999, absolute=False, duration=0.2)
        mouse.move(1822,960, absolute=False, duration=0.2)
        mouse.click('left')
        time.sleep(0.5)
        break
    else:
        print ("I am unable to see it")
        time.sleep(0.5)
        break

        
