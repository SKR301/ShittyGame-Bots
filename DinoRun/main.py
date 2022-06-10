"""
A python GUI bot to play 'dino run'
"""
import pyautogui
import keyboard

lookupPixPos1 = {'x': 775, 'y': 310}
lookupPixPos2 = {'x': 777, 'y': 310}
lookupPixPos3 = {'x': 780, 'y': 310}
bgPixPos = {'x': 10, 'y': 500}

# def jump():
#     pyautogui.keyUp('down')
#     pyautogui.keyDown('space')
#     pyautogui.keyUp('space') 
#     time.sleep(0.1)
#     pyautogui.keyDown('down')


while keyboard.is_pressed('q') == False:
    lookupPixCol1 = pyautogui.pixel(lookupPixPos1['x'], lookupPixPos1['y'])
    lookupPixCol2 = pyautogui.pixel(lookupPixPos2['x'], lookupPixPos2['y'])
    lookupPixCol3 = pyautogui.pixel(lookupPixPos3['x'], lookupPixPos3['y'])
    bgPixCol = pyautogui.pixel(bgPixPos['x'], bgPixPos['y'])
    
    # pyautogui.keyDown('down')

    # jump on cactus 
    if lookupPixCol1 != bgPixCol or lookupPixCol2 != bgPixCol or lookupPixCol3 != bgPixCol:     
        # jump()
        pyautogui.keyDown('space')
        pyautogui.keyUp('space') 
