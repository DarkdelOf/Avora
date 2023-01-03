import time
import pyautogui

timeout = time.time() + 3   # 5 minutes from now
while True:
    test = 0
    pyautogui.typewrite('vai toma no cu')
    pyautogui.press('enter')
    if test == 5 or time.time() > timeout:
        break
    test = test - 1