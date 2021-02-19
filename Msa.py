from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Title 1 Position:  X: 1872  Y: 1007 RGB: ( 124, 22, 22)
#Title 2 Position:  X: 1856  Y: 952 RGB: ( 76, 76, 76)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #pauses script for 0.01 seconds!
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1872, 1007) [0] == 0:
        click(1872, 1007)     
    if pyautogui.pixel(1856, 952) [0] == 0:
        click(1856, 952)


