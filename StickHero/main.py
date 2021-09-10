"""
A python GUI bot to play 'stick hero'
"""

import pyautogui
from PIL import Image
import time
from numpy import asarray
import win32api, win32con
import keyboard

platformColor = (41,29,20)					#platform colour(rgb)
y = 467

frame = (753, 133, 336, 600)				#game window
pxPerSec = 250								#Bridge pixels/Sec

def click(clickDuration):
	pyautogui.moveTo(853, 233)				#random position in frame
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(clickDuration)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
	ss = pyautogui.screenshot('frame.png', region = frame)
	pixels = asarray(Image.open('frame.png'))

	cliff1 = True
	cliff1End = 0 
	cliff2Start = 0 
	cliff2End = 0 
	for x in range(1, frame[3]):			#scan the width of window
		if cliff1 and pixels[y][x][0] != platformColor[0] and pixels[y][x][1] != platformColor[1] and pixels[y][x][2] != platformColor[2] and pixels[y][x-1][0] == platformColor[0] and pixels[y][x-1][0] == platformColor[0] and pixels[y][x-1][0] == platformColor[0]:
			cliff1End = x
			cliff1 = False

		if pixels[y][x][0] == platformColor[0] and pixels[y][x][1] == platformColor[1] and pixels[y][x][2] == platformColor[2] and pixels[y][x-1][0] != platformColor[0] and pixels[y][x-1][0] != platformColor[0] and pixels[y][x-1][0] != platformColor[0]:
			cliff2Start = x

		if not cliff1 and pixels[y][x][0] != platformColor[0] and pixels[y][x][1] != platformColor[1] and pixels[y][x][2] != platformColor[2] and pixels[y][x-1][0] == platformColor[0] and pixels[y][x-1][0] == platformColor[0] and pixels[y][x-1][0] == platformColor[0]:
			cliff2End = x

	barLength = (cliff2Start - cliff1End) + ((cliff2End - cliff2Start) / 2)
	clickDuration = barLength / pxPerSec		

	click(clickDuration)

	time.sleep(3)