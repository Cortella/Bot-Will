# -*- coding: utf-8 -*-
"""
Created on Sat May 9 19:17:31 2020

@author: cortella
"""

from time import sleep
from libs.estruturas import get_posicoes
from libs.estruturas import get_contas
from libs.menu import menu

contas = get_contas()
posicoes = get_posicoes()
while True:
    menu()
    opcao = int(input('Digite a opcao desejada: '))
    sleep(	1)
    if opcao == 1:
        print('Executando farm')
        sleep(2)
    elif opcao == 2:
        print('Obrigado por usar o Will - Hora de dormir!')
        sleep(2)
        break;
    else:
        print('Opcao invalida! \n Digite uma opcao valida.')
       sleep(2)

    


    
        
  

    


