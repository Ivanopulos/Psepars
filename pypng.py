import cv2
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui #pip install opencv-python для pyautogui.locateOnScreen('link.png', region=(x, y-30, 600, 55), confidence=0.95)"
import time
from array import *

#variable_name = array(pyscreeze.Box, [10])
ts = 0.4
ppaus = 1
for i in range(40):  # переформ по шаблону очень плохо работает с прокруткой pip install opencv-python
    for u in range(1, 9):
        print(i)
        print("-")
        print(u)
        t = 0
        while t == 0:
            pprint = pyautogui.locateOnScreen(str(u)+'.png')
            time.sleep(ts)
            if not pprint is None:
                t=1
        if pprint.top > 800 and u == 1:  # down
            pyautogui.scroll(-150)
            time.sleep(ts/2)
            pprint = pyautogui.locateOnScreen(str(u) + '.png')
            time.sleep(ts / 2)
        pyautogui.moveTo(pprint)
        if u == 1:  # проверка на дозагруз страницы
            t = 0
            while t == 0:
                pyautogui.click()
                time.sleep(ts / 2)
                print(1)
                pprint2 = pyautogui.locateOnScreen(str(u) + '.png')
                if not pprint2 == pprint and pprint2 is not None:  # при условии что работал клик координаты должны отличаться

                    t = 1
                    print(pprint)
                    print(pprint2)
        else:
            pyautogui.click()

        #if u == 6:
        #    pyautogui.write('.')
        time.sleep(ts)
    time.sleep(ppaus)