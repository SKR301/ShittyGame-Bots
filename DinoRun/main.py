"""
A python GUI bot to play 'dino run'
"""
import time
import pyautogui
import keyboard

lookupPixPos = {'x': 775, 'y': 310}
dinoPixPos = {'x': 675, 'y': 310}
bgPixPos = {'x': 10, 'y': 500}
spFactor = 0.01

while keyboard.is_pressed('q') == False:
    lookupPixCol = pyautogui.pixel(lookupPixPos['x'], lookupPixPos['y'])
    bgPixCol = pyautogui.pixel(bgPixPos['x'], bgPixPos['y'])
    dinoPixCol = pyautogui.pixel(dinoPixPos['x'], dinoPixPos['y'])

    # jump on cactus
    if lookupPixCol != bgPixCol:
        keyboard.press_and_release('space')
        print('jump')

    # crouch on dragon
