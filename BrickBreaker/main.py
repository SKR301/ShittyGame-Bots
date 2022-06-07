"""
A python GUI bot to play 'brick breakers'
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

gameFrame = {"startX":587,"startY":310,"endX":1241,"endY":821}					#setting game frame pixels
elementPixel = {"r":255,"g":255,"b":255}											# RGB value to find and click

while keyboard.is_pressed("q") == False:	
    pic = pyautogui.screenshot(region=(gameFrame["startX"],gameFrame["startY"],gameFrame["endX"],gameFrame["endY"]))
    width,height = pic.size

    for x in range (gameFrame["startX"], gameFrame["endX"], 5):					#loop through the whole game frame
        for y in range (gameFrame["startY"],gameFrame["endY"], 5):
            # r,g,b = pic.getpixel((x,y))
            # if r == elementPixel["r"] and b == elementPixel["b"] and g == elementPixel["g"]:
            #     pixel = {"x":x+gameFrame["startX"],"y":y+gameFrame["startY"]}		#setting pixel to click (adding offset)
            #     pyautogui.moveTo(pixel["x"], pixel["y"])
            #     break
            # print(r,g,b)
            pyautogui.moveTo(x,y)