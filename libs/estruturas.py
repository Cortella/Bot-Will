def get_posicoes():
    with open('posicao.txt','r') as arquivo:
        posicoes = {}
        for linha in arquivo:
            cortado = linha.split(',')
            cortado[2] = cortado[2].rstrip()
            cortado[1] = int(cortado[1])
            cortado[2] = int(cortado[2])
            pos=(cortado[1],cortado[2])
            posicoes[cortado[0]] = pos
            
    return posicoes