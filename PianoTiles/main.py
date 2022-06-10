"""
A python GUI bot to play 'piano tiles'
"""

import pyautogui
import time
import keyboard
import win32api, win32con

firstTile = {"x":550,"y":550};		#postion of 1st tile
secondTile = {"x":650,"y":550};		#postion of 2nd tile
thirdTile = {"x":750,"y":550};		#postion of 3rd tile
forthTile = {"x":850,"y":550};		#postion of 4th tile

def click(pixel):
	win32api.SetCursorPos((pixel["x"],pixel["y"]))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(0.01)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	if pyautogui.pixel(firstTile["x"],firstTile["y"])[0] == 0:
		click(firstTile)
	if pyautogui.pixel(secondTile["x"],secondTile["y"])[0] == 0:
		click(secondTile)
	if pyautogui.pixel(thirdTile["x"],thirdTile["y"])[0] == 0:
		click(thirdTile)
	if pyautogui.pixel(forthTile["x"],forthTile["y"])[0] == 0:
		click(forthTile)