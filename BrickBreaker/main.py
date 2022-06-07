"""
A python GUI bot to play 'brick breakers'
"""

from pyautogui import *
import pyautogui
import keyboard

gameFrame = {"startX":580,"startY":620,"endX":1240,"endY":820}					#setting game frame pixels

while keyboard.is_pressed("q") == False:
    try:
        ballLoc = pyautogui.locateOnScreen('ball.png', region=(gameFrame["startX"],gameFrame["startY"],gameFrame["endX"],gameFrame["endY"]), confidence=0.7)
        ballX, ballY = pyautogui.center(ballLoc)
        pyautogui.moveTo(ballX, ballY)
    except:
        print()