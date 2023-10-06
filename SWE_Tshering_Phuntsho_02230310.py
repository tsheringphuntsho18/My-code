import pyautogui
import time
text='oie jabu tu'
time.sleep(5)
x=5
while x > 0:
    time.sleep(5)
    pyautogui.typewrite(text)
    time.sleep(2)
    pyautogui.press('enter')
    x-=1
