from tkinter import *
import time

janela = Tk()

cor1="#1a1a1a"
cor2="#fafcff"
cor3="#21c25c"
cor4="#eb463b"
cor5="#dedcdc"
cor6="#3080f0"
contador = 0




def muda():
    for i in range(1000):
        time.sleep(1)
        la = Label(janela,text='01',bg=cor1,fg='white').place(x=250,y=200)
        janela.update()
        time.sleep(1)
        janela.update()
        la = Label(janela,text='02',bg=cor2).place(x=250,y=200)
        janela.update()
        time.sleep(1)
        la = Label(janela,text='03',bg=cor3).place(x=250,y=200)
        janela.update()
        time.sleep(1)
        janela.update()
        la = Label(janela,text='04',bg=cor4).place(x=250,y=200)
        time.sleep(1)
        janela.update()
        la = Label(janela,text='05',bg=cor5).place(x=250,y=200)
        janela.update()
        time.sleep(1)
        la = Label(janela,text='06',bg=cor6).place(x=250,y=200)
        janela.update()
        time.sleep(1)
        la = Label(janela,text='final do loop',bg=cor1,fg='orange').place(x=350,y=235)
        janela.update()
        la = Label(janela,text='final do loop',bg=cor6,fg='orange').place(x=350,y=235)
        time.sleep(1)
        janela.update
        
  
        janela.update()
        
        print(i)
        
        
        



bd = Button(janela,text='muda',command=muda).pack()


janela.title("Enigma")
janela.geometry("600x600")
janela.mainloop()  



                        




