from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (189,  44,  49)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(1920,1080,1920,1080))

    width, height = pic.size
    
for x in range (0,1920,5):
    for y in range(0,1080,5):

        r,g,b = pic.getpixel((x,y))

        if b == 49:
                click
                time.sleep(0.05)
                break
