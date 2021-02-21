import sys
import pyautogui
from tkinter import *
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse
import runpy
from tkinter import messagebox
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["tkinter"]}
build_exe_options = {"includes": ["pyautogui"]}
build_exe_options = {"includes": ["time"]}
build_exe_options = {"includes": ["keyboard"]}
build_exe_options = {"includes": ["random"]}
build_exe_options = {"includes": ["win32api, win32con"]}
build_exe_options = {"includes": ["mouse"]}
build_exe_options = {"includes": ["messagebox"]}
build_exe_options = {"includes": ["runpy"]}




# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "simple_Tkinter",
    version = "0.1",
    description = "Sample cx_Freeze Tkinter script",
    options = {"build_exe": build_exe_options},
    executables = [Executable("the timer.py", base = base)])

setup(  name = "ZoomIdle",
        version = "3.0",
        description = "A application that lets you AFK zooms",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ZoomIdle.py"), Executable("ZoomMain.py")])
