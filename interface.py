from tkinter import *
from tkinter import ttk
from exercicios import PlanilhaDeExercicio
from treino import Treino

ie = PlanilhaDeExercicio()
it = Treino()

janela = Tk()
janela.geometry("600x300")
janela.resizable(height=False, width=False)
janela.config(bg="#333333")
janela.title("Sistema de gerenciamento de treinos")
janela.iconbitmap('gym_86590.ico')

inicial = Frame(janela)
exercicios = Frame(janela)
treinos = Frame(janela)
sobre = Frame(janela)
texto = "Bem vindo(a) ao sistema de gerenciamento de treinos!"
texto_bem_vindo = Label(janela, text=texto, padx=50, pady=15, bg='#333333', fg='white', font=("Arial", 12))
texto_bem_vindo.grid(column=1, row=0)


def pagina_inicial():
    exercicios.grid_forget()
    treinos.grid_forget()
    sobre.grid_forget()
    texto_bem_vindo.grid(column=1, row=0)
    inicial.grid()

    
def pagina_exercicios():
    inicial.grid_forget()
    exercicios.grid()
    exercicios.config(bg="#333333")
    texto = "                              Exercícios"
    texto_exercicios = Label(exercicios, text=texto, padx=50, pady=10, bg='#333333', fg='white', font=("Arial", 12))
    texto_exercicios.grid(column=1, row=0)
    texto_bem_vindo.grid_forget()

    texto_embranco = Label(exercicios, text="  ", pady=10, bg='#333333')
    texto_embranco.grid(column=1, row=1)
    #---------------------Entradas-página-de-exercícios---------------------------#"
    # Cadastrar
    cadastrar = Button(exercicios, text="Cadastrar", bg='#D2691E', command=lambda: ie.cadastrar(entrada_cadastrar.get(), descricao_cadastrar.get()))
    cadastrar.grid(column=1, row=2, sticky='w')
    entrada_cadastrar = ttk.Entry(exercicios)
    entrada_cadastrar.grid(column=1, row=2, padx=10, pady=5)
    entrada_cadastrar.insert(0, "Exercício")
    descricao_cadastrar = ttk.Entry(exercicios)
    descricao_cadastrar.grid(column=2, row=2, padx=10, pady=5)
    descricao_cadastrar.insert(0, "Descrição")

    # Excluir
    excluir = Button(exercicios, text="Excluir", padx=9, bg='#D2691E', command=lambda: ie.excluir(entrada_excluir.get()))
    excluir.grid(column=1, row=3, sticky='w')
    entrada_excluir = ttk.Entry(exercicios)
    entrada_excluir.grid(column=1, row=3, padx=10, pady=5)
    entrada_excluir.insert(0, "Exercício")

    # busca
    busca = Button(exercicios, text="Buscar", padx=9, bg='#D2691E', command=lambda: ie.busca(entrada_busca.get()))
    busca.grid(column=1, row=4, sticky='w')
    entrada_busca = ttk.Entry(exercicios)
    entrada_busca.grid(column=1, row=4, padx=10, pady=5)
    entrada_busca.insert(0, "Exercício")

    # Atualiza
    atualiza = Button(exercicios, text="Atualizar", padx=3, bg='#D2691E', command=lambda: ie.atualizar(entrada_atualiza.get(), descricao_atualiza.get()))
    atualiza.grid(column=1, row=5, sticky='w')
    entrada_atualiza = ttk.Entry(exercicios)
    entrada_atualiza.grid(column=1, row=5, padx=10, pady=5)
    entrada_atualiza.insert(0, "Exercício")
    descricao_atualiza = ttk.Entry(exercicios)
    descricao_atualiza.grid(column=2, row=5, padx=10, pady=5)
    descricao_atualiza.insert(0, " Nova descrição")

   # Listagem
    listagem = Button(exercicios, text="Listagem", padx=2, bg='#D2691E', command=lambda: ie.listagem())
    listagem.grid(column=1, row=6, sticky='w')


def pagina_treinos():
    inicial.grid_forget()
    treinos.grid()
    treinos.config(bg="#333333")
    texto = "                              Treinos"
    texto_treinos = Label(treinos, text=texto, padx=50, pady=10, bg='#333333', fg='white', font=("Arial", 12))
    texto_treinos.grid(column=1, row=0)
    texto_bem_vindo.grid_forget()

    texto_embranco = Label(treinos, text="  ", pady=10, bg='#333333')
    texto_embranco.grid(column=1, row=1)
    
    # Cadastrar
    cadastrar = Button(treinos, text="Cadastrar", bg='#D2691E', command=lambda: it.cadastrar(nome_treino.get(), idade_treino.get(), altura_treino.get(), peso_treino.get(), dias_treino.get()))
    cadastrar.grid(column=1, row=2, sticky='w')
    nome_treino = ttk.Entry(treinos, width=15)
    nome_treino.place(x=178, y=88)
    nome_treino.insert(0, "nome do treino")

    idade_treino = ttk.Entry(treinos, width=5)
    idade_treino.place(x=290, y=88)
    idade_treino.insert(0, "idade")

    altura_treino = ttk.Entry(treinos, width=5)
    altura_treino.place(x=340, y=88)
    altura_treino.insert(0, "altura")

    peso_treino = ttk.Entry(treinos, width=5)
    peso_treino.place(x=390, y=88)
    peso_treino.insert(0, "peso")

    dias_treino = ttk.Entry(treinos, width=15)
    dias_treino.place(x=440, y=88)
    dias_treino.insert(0, "dias de treino")

    # Excluir
    excluir = Button(treinos, text="Excluir", padx=9, bg='#D2691E', command=lambda: it.remove(entrada_excluir.get()))
    excluir.grid(column=1, row=3, sticky='w')
    entrada_excluir = ttk.Entry(treinos)
    entrada_excluir.grid(column=1, row=3, padx=10, pady=5)
    entrada_excluir.insert(0, "treino")

    # busca
    busca = Button(treinos, text="Buscar", padx=9, bg='#D2691E', command=lambda: it.busca(entrada_busca.get()))
    busca.grid(column=1, row=4, sticky='w')
    entrada_busca = ttk.Entry(treinos)
    entrada_busca.grid(column=1, row=4, padx=10, pady=5)
    entrada_busca.insert(0, "treino")

   # Listagem
    listagem = Button(treinos, text="Listagem", padx=2, bg='#D2691E', command= it.listagem)
    listagem.grid(column=1, row=5, sticky='w')
    correcao = Label(treinos, text='   ', padx=80, pady=2, bg="#333333").grid(column=2, row=4)

def pagina_sobre():
    inicial.grid_forget()
    sobre.grid()
    sobre.config(bg="#333333")
    texto_bem_vindo.grid_forget()
    texto = "Sobre"
    texto_sobre = Label(sobre, text=texto, padx=210, pady=13, bg='#333333', fg='white', font=("Arial", 12))
    texto_sobre.grid(column=1, row=0)
    texto2 = "Esse projeto é um sistema que gerencia treinos.\nEle foi feito pelos alunos de Engenharia de Computação\nGabriel De Paula, Luíz Felipe Chagas e Rafael Barbosa Lindquist."
    texto_sobre2 = Label(sobre, text=texto2, padx=50, pady=10, bg='#333333', fg="white")
    texto_sobre2.grid(column=1, row=1)

    imagem = PhotoImage(file="imagem_projeto.png")
    foto = Label(sobre, image=imagem)
    foto.imagem = imagem
    foto.grid(column=1, row=2)

btao_exercicios = Button(inicial, text="Exercícios", command=pagina_exercicios, bg='#D2691E', padx=20, pady=10)
btao_exercicios.grid(column=0, row=1)

btao_treinos = Button(inicial, text="Treinos", command=pagina_treinos, bg='#D2691E', padx=27, pady=10)
btao_treinos.grid(column=0, row=2)

btao_sobre = Button(inicial, text="Sobre", command=pagina_sobre, bg='#D2691E', padx=31, pady=10)
btao_sobre.grid(column=0, row=3)

btao_inicial = Button(exercicios, text="Inicial", command=pagina_inicial, bg='#D2691E', padx=31, pady=10)
btao_inicial.grid(column=0, row=0)

btao_inicial = Button(treinos, text="Inicial", command=pagina_inicial, bg='#D2691E', padx=31, pady=10)
btao_inicial.grid(column=0, row=0)

btao_inicial = Button(sobre, text="Inicial", command=pagina_inicial, bg='#D2691E', padx=31, pady=10)
btao_inicial.grid(row=0, column=0)

inicial.grid()

janela.mainloop()