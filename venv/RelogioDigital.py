import tkinter as tk
import time
def atualiza():
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    meses = (
    '', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
    'Dezembro')
    agora = time.strftime("%H:%M:%S")
    dataAgora = time.strftime('%d/%B/%Y')
    if lbSec['text'] != agora or lbData['text'] != dataAgora:
        lbSec['text']= agora
        lbData['text'] = dataAgora
    lbSec.after(1, atualiza)
janela = tk.Tk()
janela.geometry("800x600+100+100")
lbSec = tk.Label(bg=janela['bg'], fg="Red", text=time.strftime("%H:%M:%S"), font ="Arial 48")
lbData= tk.Label(bg =janela['bg'], fg='Blue', text= time.strftime('%d/%B/%Y'), font = "Arial 40")
lbSec.place(x=200, y=100)
lbData.place(x=200, y=200)
atualiza()
janela.mainloop()