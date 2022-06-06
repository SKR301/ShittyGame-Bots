"""
A python GUI bot to play 'brick breakers'
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

gameFrame = {"startX":500,"startY":100,"endX":1095,"endY":680}					#setting game frame pixels
elementPixel = {"r":69,"g":116,"b":176}											# RGB value to find and click

while keyboard.is_pressed("q") == False:	
	pic = pyautogui.screenshot(region=(gameFrame["startX"],gameFrame["startY"],gameFrame["endX"],gameFrame["endY"]))
	width,height = pic.size

	for x in range (gameFrame["startX"], gameFrame["endX"], 10):					#loop through the whole game frame
		for y in range (gameFrame["startY"],gameFrame["endY"], 10):
			r,g,b = pic.getpixel((x,y))
			if r == elementPixel["r"]:
				pixel = {"x":x+gameFrame["startX"],"y":y+gameFrame["startY"]}		#setting pixel to click (adding offset)
				click(pixel)
				break