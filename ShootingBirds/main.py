"""
A python GUI bot to play 'shooting birds'
"""

import pyautogui
import keyboard
import win32api, win32con

gameFrame = {"startX":400,"startY":225,"endX":1000,"endY":600}					#setting game frame pixels
elementPixel = {"r":236,"g":28,"b":36}											# RGB value to find and click


def click(pixel):
	win32api.SetCursorPos((pixel["x"],pixel["y"]))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

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