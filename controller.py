# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:28:39 2020

@author: cortella
"""

#DEIXE O APLICATIVO NA TELA DE SELECÇÃO DE SERVIDORES
#V1.0 -> feito para telas de resolução 1366x768
#configure o aplicativo para ocupar toda a tela antes de rodar

#define ID cortellapedras
#define senha Dest@quemito10


#importa biblioteca de controle de maquina
import pyautogui

#importa biblioteca de temporazicao
import time

#mapeia tela em pixels e convente em coordenadas cartesianas
x , y = pyautogui.size()

#get coordenadas do mouse (pixels)
mouseP1 , mouseP2 = pyautogui.position()
print(mouseP1)
print(mouseP2)

time.sleep(2)

#Move mouse para coordenada especifica
pyautogui.moveTo(1009,750)
time.sleep(1)
pyautogui.click()

time.sleep(1)

pyautogui.moveTo(810,621)
time.sleep(1)
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(713,346)
pyautogui.click()

pyautogui.write()

#810,621
#713,346