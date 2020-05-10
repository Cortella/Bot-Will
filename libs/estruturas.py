def get_posicoes():
    posicoes = {}
    try:  
        with open('posicao.txt','r') as arquivo:        
            for linha in arquivo:
                cortado = linha.split(',')
                cortado[2] = cortado[2].rstrip()
                cortado[1] = int(cortado[1])
                cortado[2] = int(cortado[2])
                pos = (cortado[1], cortado[2])
                posicoes[cortado[0]] = pos
            arquivo.close()
            print('teste')
            
                
    except IOError:
        print('O arquivo nao existe no diretorio ou nao foi reconhecido')
    else:
        return posicoes


