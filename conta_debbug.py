# -*- coding: utf-8 -*-
from libs.estruturas import get_contas
from libs.estruturas import get_posicoes
from Entities.Conta import Conta

contas = get_contas()
posicoes = get_posicoes()

print(contas.keys)

