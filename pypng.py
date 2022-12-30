import cv2
import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui #pip install opencv-python для pyautogui.locateOnScreen('link.png', region=(x, y-30, 600, 55), confidence=0.95)"
import time
from array import *

#variable_name = array(pyscreeze.Box, [10])
ts = 1
ppaus = 1
# for i in range(40): # резолюция согласовано
#     for u in range(1, 13):
#         print(i)
#         print("-")
#         print(u)
#         t = 0
#         while t == 0:
#             pprint = pyautogui.locateOnScreen(str(u)+'.png')
#             time.sleep(ts)
#             if not pprint is None:
#                 t=1
#         if pprint.top > 600 and u == 1:  # down
#             pyautogui.scroll(-100)
#             time.sleep(ts/2)
#             pprint = pyautogui.locateOnScreen(str(u) + '.png')
#             time.sleep(ts / 2)
#         pyautogui.moveTo(pprint)
#         t=0
#         if u==7:
#             while t == 0:
#                 pprint1 = pyautogui.locateOnScreen(str(u) + '.png')
#                 time.sleep(ts)
#                 if pprint1 is None:
#                     t = 1
#         pyautogui.click()
#         #if u == 6:
#         #    pyautogui.write('.')
#         time.sleep(ts)
#     time.sleep(ppaus)


for i in range(20): #переформ по шаблону очень плохо работает с прокруткой pip install opencv-python

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
        if u == 1: #проверка на дозагруз страницы
            t=0
            while t==0:
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








# for i in range(20):
#     for u in range(1, 14):
#         print(i)
#         print("-")
#         print(u)
#         t = 0
#         while t == 0:
#             pprint = pyautogui.locateOnScreen(str(u)+'.png')
#             time.sleep(ts)
#             if not pprint is None:
#                 t=1
#         if pprint.top > 600 and u == 1:  # down
#             pyautogui.scroll(-170)
#             time.sleep(ts/2)
#             pprint = pyautogui.locateOnScreen(str(u) + '.png')
#             time.sleep(ts / 2)
#         pyautogui.moveTo(pprint)
#         pyautogui.click()
#         if u == 6:
#             pyautogui.write('.')
#         time.sleep(ts)



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
