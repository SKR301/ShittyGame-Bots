"""
A python GUI bot to play 'dino run'
"""
import pyautogui
import time
import keyboard

lookupPixPos = {'x': 734, 'y': 308}
bgPixPos = {'x': 0, 'y': 500}

while keyboard.is_pressed('q') == False:
    lookupPixCol = pyautogui.pixel(lookupPixPos['x'], lookupPixPos['y'])
    bgPixCol = pyautogui.pixel(bgPixPos['x'], bgPixPos['y'])

    print(lookupPixCol, bgPixCol)

    # jump on cactus
    if lookupPixCol != bgPixCol:
        # keyboard.press_and_release('space')
        print('jump')

    # crouch on dragon
