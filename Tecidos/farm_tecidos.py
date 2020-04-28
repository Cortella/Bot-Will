# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:32:23 2020

@author: cortella
"""

#Farm with mt2-Module V1.0
#Tecidos

import time
import pyautogui
print("--------- Bem vindo ao modulo de farm de de tecidos ---------------")
print("\n Primeiramente voce deve se certificar que a tela esta corretamente posicionada, do contrario o promagra não funcionara corretamente")
print("\n Uma imagem de exemplo esta disponivel na pasta do modulo")
print("A posicao incial dou mouse depende da resolucao da saída de video")
check = input("Digite 's' para iniciar, ou 'e' para finilizar: ")
while (check !='s'):
    check = input("Digite 's' para iniciar, ou 'e' para finilizar: ")
    if(check == 'e'):
        break
print("Inciando...")

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

seconds = time.time()
local_time = time.ctime(seconds)
print("Instante do click = " + local_time)




print("Time:"+ local_time)
