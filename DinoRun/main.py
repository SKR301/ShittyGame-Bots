"""
A python GUI bot to play 'dino run'
"""
import pyautogui
import time
import keyboard

lookupPixPosBL = {'x': 740, 'y': 310}
bgPixPos = {'x': 0, 'y': 500}

while keyboard.is_pressed('q') == False:
    lookupPixColBL = pyautogui.pixel(lookupPixPosBL['x'], lookupPixPosBL['y'])
    bgPixCol = pyautogui.pixel(bgPixPos['x'], bgPixPos['y'])

    # jump on cactus
    if lookupPixColBL != bgPixCol:
        keyboard.press_and_release('space')
        print('jump')

    # crouch on dragon
