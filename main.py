import pyautogui
import time
from libs.estruturas import get_posicoes

posicoes = get_posicoes()
time.sleep(2)
pyautogui.moveTo(posicoes['opcoesJogo'])     
        



