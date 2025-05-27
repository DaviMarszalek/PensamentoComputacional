import tkinter as tk
'''
janela = tk.Tk()
janela.title("Minha Primeira Janela")
rotulo = tk.Label(janela, text="Bem Vindo ao Tkinter!", font=("Arial",16))
rotulo.pack(padx=20, pady=20)
janela.geometry("300x200")
janela.mainloop()'''

cont = 0

def clique():
    global cont
    if cont == 0:
        rotulo.config(text=f"Olá, Mundo!")
        cont += 1
    elif cont == 1:
        rotulo.config(text=f"Olá, Turma!")
        cont += 1
    elif cont == 2:
        rotulo.config(text=f"Olá, Amigos!")
        cont = 0 
    
janela = tk.Tk()
janela.title("Exemplo botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text="Clique no botão abaixo", font=("Arial", 16))
rotulo.pack(pady=10)
botao = tk.Button(janela, text="Clique aqui", command=clique, font=("Arial", 14))

botao.pack(pady=10)
janela.mainloop()   
