# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:25:44 2020

@author: bnmac
"""

import pyautogui
import time

for i in range(15):
    print("Inciando... ", i )
    time.sleep(1)
w,h = pyautogui.size()
wr,hr = 733,108
wAurea, hAurea = 893,611
wLamina, hLamina = 916,606
wCiclone,hCiclone =  956,603
wMedo,hMedo = 1037,610
wDef,hDef = 1063,604
wAtk,hAtk = 1098,604
wXp,hXp = 1132,604

for i in range (16):
    print("Stage pot ", i)
    pyautogui.moveTo(wXp,hXp,0.25)
    pyautogui.click(button='right')
    time.sleep(0.5)
    pyautogui.moveTo(wAtk,hAtk,0.25)
    pyautogui.click(button='right')
    time.sleep(0.5)
    pyautogui.moveTo(wDef,hDef,0.25)
    pyautogui.click(button='right')
    time.sleep(0.5)
    for j in range(12):
        print("skill Stage = ",j)
        pyautogui.moveTo(wAurea,hAurea,0.25)
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.moveTo(wLamina,hLamina,0.25)
        pyautogui.click(button='right')
        time.sleep(2)
        pyautogui.moveTo(wMedo,hMedo,0.25)
        pyautogui.click(button='right')
        time.sleep(2)
        for z in range(300):
            pyautogui.press('U')
            time.sleep(0.2)
        pyautogui.moveTo(wr,hr,0.25)
        pyautogui.click(button='left')
        for z in range(300):
            pyautogui.press('U')
            time.sleep(0.2)
        pyautogui.moveTo(wr,hr,0.25)
        pyautogui.click(button='left')
        for z in range(113):
             pyautogui.press('U')
             time.sleep(0.2)
        
    