import tkinter as tk
'''
janela = tk.Tk()
janela.title("Minha Primeira Janela")
rotulo = tk.Label(janela, text="Bem Vindo ao Tkinter!", font=("Arial",16))
rotulo.pack(padx=20, pady=20)
janela.geometry("300x200")
'''

"""cont = 0

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

botao.pack(pady=10)   """

'''def mostrar_texto():
    texto = entrada.get()
    rotulo.config(text=f"Você digitou: {texto}")
    
janela = tk.Tk()   
janela.title("Exemplo Entry") 
janela.geometry("300x200")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Exibir", command=mostrar_texto)
botao.pack(pady=10)

rotulo = tk.Label(janela, text="")
rotulo.pack(pady=5)'''

'''def mostrar_estado():
    if var.get():
        rotulo.config(text="Selecionado!")
    else:
        rotulo.config(text="Não selecionado.")
        
janela = tk.Tk()
janela.title("Exemplo Checkbutton")
janela.geometry("250x120")
var = tk.BooleanVar()
check = tk.Checkbutton(janela, text="Opção", variable=var, command=mostrar_estado)
check.pack(pady=10)
rotulo = tk.Label(janela, text="Não selecionado.")
rotulo.pack(pady=5)'''


'''def mostrar_opcao():
    rotulo.config(text=f"Escolheu: {opcao.get()}")
    
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")

opcao = tk.StringVar(value="A")
tk.Radiobutton(janela, text="Tempo", variable=opcao, value="A", command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Dinheiro", variable=opcao, value="B", command=mostrar_opcao).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao, value="C", command=mostrar_opcao).pack()

rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)

janela.mainloop()'''

def mostrar_opcao(botao):
    texto = f"Escolheu: {opcao1.get()}"
    texto += f"{opcao2.get()}"  
    texto += f"{opcao3.get()}"   
    rotulo.config(text=texto)
    
    if opcao1.get() and opcao2.get() and opcao3.get():
        if botao == "Tempo":
            opcao2.set(False)
        if botao == "Dinheiro":
            opcao3.set(False)
        if botao == "Saúde":
            opcao1.set(False)        
    
janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("600x400")

opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Radiobutton(janela, text="Tempo", variable=opcao1, value=True, command=lambda : mostrar_opcao("Tempo")).pack()
tk.Radiobutton(janela, text="Dinheiro", variable=opcao2, value=True, command=lambda : mostrar_opcao("Dinheiro")).pack()
tk.Radiobutton(janela, text="Saúde", variable=opcao3, value=True, command=lambda : mostrar_opcao("Saúde")).pack()

rotulo = tk.Label(janela, text="Escolheu")
rotulo.pack(pady=10)

janela.mainloop()


