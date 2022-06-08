"""
A python GUI bot to play 'dino run'
"""
import pyautogui
import time
import keyboard

lookupPixPosBL = {'x': 740, 'y': 310}
# lookupPixPosTL = {'x': 735, 'y': 300}
# lookupPixPosTR = {'x': 745, 'y': 300}
# lookupPixPosBR = {'x': 745, 'y': 310}
# lookupPixPosC = {'x': 740, 'y': 305}
bgPixPos = {'x': 0, 'y': 500}

while keyboard.is_pressed('q') == False:
    lookupPixColBL = pyautogui.pixel(lookupPixPosBL['x'], lookupPixPosBL['y'])
    # lookupPixColTL = pyautogui.pixel(lookupPixPosTL['x'], lookupPixPosTL['y'])
    # lookupPixColTR = pyautogui.pixel(lookupPixPosTR['x'], lookupPixPosTR['y'])
    # lookupPixColBR = pyautogui.pixel(lookupPixPosBR['x'], lookupPixPosBR['y'])
    # lookupPixColC = pyautogui.pixel(lookupPixPosC['x'], lookupPixPosC['y'])
    bgPixCol = pyautogui.pixel(bgPixPos['x'], bgPixPos['y'])

    # print(lookupPixColBL, lookupPixColTL, lookupPixColTR, lookupPixColBR, lookupPixColC, bgPixCol)

    # jump on cactus
    # if lookupPixColBL != bgPixCol or lookupPixColTL != bgPixCol or lookupPixColTR != bgPixCol or lookupPixColBR != bgPixCol or lookupPixColC != bgPixCol:
    if lookupPixColBL != bgPixCol:
        keyboard.press_and_release('space')
        print('jump')

    # crouch on dragon
