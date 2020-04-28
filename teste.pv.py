# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:18:22 2020

@author: bnmac
"""

import pyautogui
import time

potXp = '1'
defesa = '2'
escudo = '3'
olhos = '4'
reflect = 'f1'
hp = 'f2'
pyautogui.hotkey('alt','tab')
for x in range(10):
    print("Programa ira iniciar " ,x)
    time.sleep(1)

for y in range(183):
    pyautogui.press('1')
    time.sleep(1)
    pyautogui.press('2')
    time.sleep(1)
    pyautogui.press('3')
    time.sleep(1)
    print("inicio skil em estagio = ",y)
    pyautogui.press(escudo);
    time.sleep(3)
    pyautogui.press(olhos);
    time.sleep(3)
    pyautogui.press(reflect);
    time.sleep(10)