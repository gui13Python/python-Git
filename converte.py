
######################## pacotes usados 
import pyautogui########################## controla o mouse e teclado
from tkinter import * #### cria a interface
import PyInstaller### converte para execultavel
import os #### utilizado para saber a pasta atual das image utilizada
from tkinter import ttk
import time################## controla o tempo



imagens = os.path.dirname(__file__)


############### funcoes 

ex = Tk()




time.sleep(2)
def Caminho():
    nome = input('digite o nome do progama : ')########### digite o nome do progama que irá ser convertido para execultavel
    pyautogui.hotkey('winleft', 'r')## abra o CMD tela de comando no Windonws
    time.sleep(2)#### espera 2 segundos
    pyautogui.write('cmd')### escreve cmd na caixa do win
    time.sleep(1)## espera 1 segundo
    pyautogui.hotkey('ENTER')########## preciona enter
    time.sleep(2) ## espera 2 segundos
    pyautogui.write('S:')############################ escreve o diretorio que esta sua pasta , neste caso em S: que é um HD separado , defina qual sera o seu 
    pyautogui.press('enter')## preciona enter
    pyautogui.write(r'cd S:\\testes e conhecimento em python\\convert en exe')#### escreve no Prompt de comando {telinha preta do wind} , é o caminha da minha pasta , escolha a sua 
    time.sleep(2)## espera 2 segundos 
    pyautogui.press('enter')########## preciona enter
    pyautogui.write('dir')################################ lista oque tem na sua pasta , para saber se o progama em python esta na pasta 
    pyautogui.hotkey('ENTER')### preciona enter
    time.sleep(5)#espera 5 segundos
    pyautogui.write('Pyinstaller --onefile'  )##### escreve , este é um modulo em python que faz a conversão para execultavel 
    pyautogui.hotkey('space')## preciona a tecla espaço para escrever o nome do arquivo em python
    pyautogui.write(nome)#### escreve o nome do arquivo em python que esta na pasta , para ser convertido em exe
    time.sleep(1)# espera 1 segundo
    pyautogui.press('enter')# pressiona a tecla enter, para começar a conversão
    exit
        #################################
        
        
    ############## tela interface
   







    ############## botao
BAK = PhotoImage(file=imagens+"\\tela.png")######################## image de fundo , que tambem é o botão
ima = Button(ex,image=BAK,bd=4,bg='#F0F0F0',command=Caminho)## botão 
ima.place(x=5,y=5) ## faz aparecer na tela o botao , e na posição que deseja
        
       ### botao 
     
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
ex.iconbitmap('exe.ico')
ex.title('CONVERSSOR PARA EXE')    
ex.configure(background='black')#F0F0F0  ############### configura cor de fundo
ex.geometry('735x600')### configura o tamanho da tela 
ex.mainloop()### deixa a tela visivel constantemente