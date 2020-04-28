# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:14:50 2020

@author: bnmac
"""

import pyautogui
import time

time.sleep(5)
w,h = pyautogui.size()
wXp,hXp = 888,626
wDef,hDef = 917,627
wEscudo , hEscudo = 953,626
wOlhos,hOlhos = 985,625
wReflect,hReflect = 1031,629
wHp,hHp = 1064,625

for x in range(10):
    print("Programa ira iniciar " ,x)
    time.sleep(1)

for j in range(180):
    print("Skill stage = ",j)
    pyautogui.moveTo(wXp,hXp,0.25)
    pyautogui.click(button = 'right')
    pyautogui.moveTo(wDef,hDef,0.25)
    pyautogui.click(button = 'right')
    pyautogui.moveTo(wEscudo,hEscudo,0.25)
    pyautogui.click(button = 'right')
    time.sleep(3)
    pyautogui.moveTo(wOlhos,hOlhos,0.25)
    pyautogui.click(button = 'right')
    time.sleep(3)
    pyautogui.moveTo(wReflect,hReflect,0.25)
    pyautogui.click(button = 'right')
    time.sleep(3)
    pyautogui.moveTo(wHp,hHp,0.25)
    pyautogui.click(button = 'right')
    time.sleep(100)
    


