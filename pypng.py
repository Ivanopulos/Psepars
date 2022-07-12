import cv2
import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui
import time
from array import *

#variable_name = array(pyscreeze.Box, [10])
for i in range(510):
    print(i)
    pprint = pyautogui.locateOnScreen('print0.png')  # print
    if pprint is None:
        time.sleep(2)
        pprint = pyautogui.locateOnScreen('print0.png')
    pyautogui.moveTo(pprint)
    pyautogui.click()
    time.sleep(0.5)
    pprint1 = pyautogui.locateOnScreen('print12.png')  # print next 1 для отчетов 12 для соглашений рп
    if pprint1 is None:
        time.sleep(2)
        pprint1 = pyautogui.locateOnScreen('print12.png')
    pyautogui.moveTo(pprint1)
    pyautogui.click()
    time.sleep(2)
    pprint2 = pyautogui.locateOnScreen('print2.png')  # load
    if pprint2 is None:
        time.sleep(4)
        pprint2 = pyautogui.locateOnScreen('print2.png')
    pyautogui.moveTo(pprint2)#1240, 302)
    pyautogui.click()
    time.sleep(1.5)
    pprint3 = pyautogui.locateOnScreen('print3.png')  # save
    if pprint3 is None:
        time.sleep(2)
        pprint3 = pyautogui.locateOnScreen('print3.png')
        qq = pprint3.top
    pyautogui.moveTo(pprint3)
    pyautogui.click()
    time.sleep(1)
    pprint4 = pyautogui.locateOnScreen('print4.png')  # close
    if pprint4 is None:
        time.sleep(2)
        pprint4 = pyautogui.locateOnScreen('print4.png')
    pyautogui.moveTo(pprint4)
    pyautogui.click()
    time.sleep(1)
    pprint5 = pyautogui.locateOnScreen('print52.png')  # next для отчетов 5 для отчетов, 52 для соглашений рп
    if pprint5 is None:
        time.sleep(2)
        pprint5 = pyautogui.locateOnScreen('print52.png')
    pyautogui.moveTo(pprint5)
    pyautogui.click()
    print(pprint5)
    if pprint5.top > 600:  # down
        pyautogui.scroll(-170)

# for i in range(210):
#     print(i)
#     pprint = pyautogui.locateOnScreen('print0.png')  # print
#     if pprint is None:
#         time.sleep(2)
#         pprint = pyautogui.locateOnScreen('print0.png')
#     pyautogui.moveTo(pprint)
#     pyautogui.click()
#     time.sleep(0.3)
#     pprint1 = pyautogui.locateOnScreen('print11.png')  # print next
#     if pprint1 is None:
#         time.sleep(1)
#         pprint1 = pyautogui.locateOnScreen('print11.png')
#         qq = pprint1.top
#     pyautogui.moveTo(pprint1)
#     pyautogui.click()
#     time.sleep(0.3)
#     pprint21 = pyautogui.locateOnScreen('print21.png')  # load
#     if pprint21 is None:
#         time.sleep(2)
#         pprint21 = pyautogui.locateOnScreen('print21.png')
#         qq = pprint21.top
#     pyautogui.moveTo(pprint21)#1240, 302)
#     pyautogui.click()
#     time.sleep(2)
#     pprint2 = pyautogui.locateOnScreen('print2.png')  # save
#     if pprint2 is None:
#         time.sleep(2)
#         pprint2 = pyautogui.locateOnScreen('print2.png')
#         qq = pprint2.top
#     pyautogui.moveTo(pprint2)
#     pyautogui.click()
#     time.sleep(1.5)
#     pprint3 = pyautogui.locateOnScreen('print31.png')  # save
#     if pprint3 is None:
#         time.sleep(2)
#         pprint3 = pyautogui.locateOnScreen('print31.png')
#         qq = pprint3.top
#     pyautogui.moveTo(pprint3)
#     pyautogui.click()
#     time.sleep(1)
#     pprint4 = pyautogui.locateOnScreen('print4.png')  # close
#     if pprint4 is None:
#         time.sleep(1)
#         pprint4 = pyautogui.locateOnScreen('print4.png')
#     pyautogui.moveTo(pprint4)
#     pyautogui.click()
#     time.sleep(0.2)
#     pprint4 = pyautogui.locateOnScreen('print4.png')  # close
#     pyautogui.moveTo(pprint4)
#     pyautogui.click()
#     time.sleep(1)
#     pprint5 = pyautogui.locateOnScreen('ordown1.png')  # для соглашений
#     if pprint5 is None:
#         pprint5 = pyautogui.locateOnScreen('ordown2.png')
#     pyautogui.moveTo(pprint5)
#     pyautogui.click()
#     print(pprint5)
#     if pprint5.top > 600:  # down
#         pyautogui.scroll(-170)
