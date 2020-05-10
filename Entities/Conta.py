import pyautogui
from time import sleep
class Conta:

    def __init__(self, login, senha, personagens):
        self.__login = login
        self.__senha = senha
        self._logado = False
        self._personagens = personagens
        
        
    @property
    def login(self):
        return self.__login
    
    @property
    def senha(self):
        return self.__senha
    
    @property
    def logado(self):
        return self._logado
    
    @property
    def personagens(self):
        return self.personagens_
    
    @logado.setter
    def logado(self,status):
        if isinstance(status,bool):
            self._logado = status
        
    def logar(self,posicoes):
        if self.logado == False:
            print('logando')
            pyautogui.moveTo(posicoes['server3'],duration = 0.25)
            pyautogui.click()
            pyautogui.moveTo(posicoes['serverOk'],duration = 0.25)
            pyautogui.click()
            pyautogui.moveTo(posicoes['id'],duration = 0.25)
            pyautogui.click()
            pyautogui.write(self.login, interval = 0.1)
            pyautogui.moveTo(posicoes['senha'],duration = 0.25)
            pyautogui.click()
            pyautogui.write(self.senha, interval = 0.1)
            pyautogui.moveTo(posicoes['conectar'],duration = 0.25)
            pyautogui.click()
        

    def fecharJogo(self,posicoes):
        if self.logado:
            print('fechando jogo')
            pyautogui.moveTo(posicoes['menu'],duration = 0.25)
            pyautogui.click()
            pyautogui.moveTo(posicoes['fecharJogo'],duration = 0.25)
            pyautogui.click()
            self.logado(False)
        else:
            print('nao foi possivel fechar o jogo, pois a conta nao esta logada!')

    def selecaoPersonagem(self,posicoes):
        if self.logado:
            print('selecionando personagem')
            pyautogui.moveTo(posicoes['menu'],duration = 0.25)
            pyautogui.click()
            pyautogui.moveTo(posicoes['selectChar'],duration = 0.25)
            pyautogui.click()
        else:
            print('nao foi possivel selecionar personagem, pois a conta nao esta logada!')
        
    def selecionarServidor(self,posicoes):
        if self.logado:
            print('selecionando servidor')
            pyautogui.moveTo(posicoes['menu'],duration = 0.25)
            pyautogui.click()
            pyautogui.moveTo(posicoes['logOut'],duration = 0.25)
            pyautogui.click()
            self.logado(False)
        else:
            print('nao foi possivel deslogar, pois a conta nao esta logada!')
            
    def selecionarPersonagem():
        pyautogui.press('\n')
