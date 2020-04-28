# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 03:17:31 2020

@author: bnmac
"""

import time
import pyautogui

w,r = pyautogui.size()

time.sleep(5)
wFuria,rFuria = 613,705
wLamina,rLamina = 649,715
wAtk,rAtk = 678,718
wDef,rDef = 710,716
wXp,rXp = 758,713

for i in range(10000):
    print("Ciclo = ",i)
    time.sleep(5)
    pyautogui.moveTo(wAtk,rAtk,0.5)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(wDef,rDef,0.5)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(wXp,rXp,0.5)
    pyautogui.click(button='right')
    time.sleep(1)
    for j in range(18):
        print("skill stage = ",j)
        pyautogui.moveTo(wLamina,rLamina,0.5)
        pyautogui.click(button='right')
        time.sleep(1)
        pyautogui.moveTo(wFuria,rFuria,0.5)
        pyautogui.click(button='right')
        for x in range(25):
            pyautogui.moveTo(wAtk,rAtk,0.5)
            pyautogui.click(button = 'right')
            time.sleep(1.5)
            pyautogui.moveTo(wDef,rDef,0.5)
            pyautogui.click(button = 'right')
            time.sleep(1.5)
        
    