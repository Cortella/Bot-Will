# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:53:43 2020

@author: bnmac
"""

import time
import pyautogui




print("Bem vindo ao programa TESTE - POT ITEM V1.03")
print("coloque seu pot red no atalho da tecla '1'")

for i in range(15,0,-1):
    print("O programa sera iniciado em " + str(i) + " Segundos")
    time.sleep(1)
print("Programa iniciado")

while(True):
    pyautogui.press('z')
    pyautogui.press('1')
    time.sleep(0.05)