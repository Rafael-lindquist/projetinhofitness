import json
import tkinter as tk
from tkinter import ttk

class Treino():
    """
    Essa classe cadastra, lista, busca, atualiza e
    remove treinos.
    """

    def cadastrar(self, nome, idade, altura, peso, dias_de_treino):
        """Essa função cadastra treinos na base de dados"""
        janela_cadastrar = tk.Tk()
        janela_cadastrar.config(bg="#333333")
        janela_cadastrar.title("Sistema de gerenciamento de treinos")
        janela_cadastrar.iconbitmap('gym_86590.ico')

        self.nome = nome
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = float(peso)
        self.dias_de_treino = int(dias_de_treino)
        treino = {self.nome: {
            'treino': {},
            'informacoes': {
                "idade": self.idade,
                "altura": self.altura,
                "peso": self.peso,
                "dias_de_treino": self.dias_de_treino
            }
        }}
        texto = f"Dia: "
        dia_treino = tk.Label(janela_cadastrar, text=texto, padx=15, pady=10, bg='#333333', fg='white')
        dia_treino.grid(column=0, row=0)
        dia_resposta = ttk.Entry(janela_cadastrar, width=20)
        dia_resposta.grid(column=1, row=0)

        exercicio = tk.Label(janela_cadastrar, text="Exercício: ", padx=15, pady=10, bg='#333333', fg='white')
        exercicio.grid(column=0, row=1)
        ex_resposta = ttk.Entry(janela_cadastrar, width=30)
        ex_resposta.grid(column=1, row=1)
        
        series = tk.Label(janela_cadastrar, text="Séries & Reps: ", padx=15, pady=10, bg='#333333', fg='white')
        series.grid(column=0, row=2)
        series_resposta = ttk.Entry(janela_cadastrar, width=30)
        series_resposta.grid(column=1, row=2)
        series_resposta.insert(0, "4x10")

        def adicionar_ex(exercicio, series, dia_r):
            exe = exercicio
            serie = series
            dia = dia_r

            if not dia in treino[self.nome]['treino']:
                treino[self.nome]['treino'][dia] = []

            with open('exercicios.json', 'r') as f:
                file = json.load(f)
            if exe in file: 
                ex = [exe, file[exe], serie]
            else:
                ex = [exe, serie]
            treino[self.nome]['treino'][dia].append(ex)

        adicionar = tk.Button(janela_cadastrar, text="Adicionar", padx=15, pady=10, bg='#D2691E', command=lambda: adicionar_ex(ex_resposta.get(), series_resposta.get(), dia_resposta.get()))
        adicionar.grid(column=0, row=3)

        def criar_treino():
            with open('treinos.json', 'r') as f:
                atualizado = json.load(f)
            atualizado.update(treino)

            with open("treinos.json", 'w') as file:
                json.dump(atualizado, file, indent=4, separators=(",", ":"))
        criar = tk.Button(janela_cadastrar, text="Criar treino", padx=15, pady=10, bg='#D2691E', command=criar_treino)
        criar.grid(column=1, row=3)

        tk.mainloop()


    def listagem(self):
        """Essa função lista os treinos existentes"""
        with open('treinos.json', 'r') as f:
            file = json.load(f)
            texto = []
            for i in file.keys():
                texto.append(i)
            texto = "\n".join(texto)
            janela_listagem = tk.Tk()
            janela_listagem.config(bg="#333333")
            janela_listagem.title("Sistema de gerenciamento de treinos")
            janela_listagem.iconbitmap('gym_86590.ico')
            label = tk.Label(janela_listagem, text=texto, bg="#333333", fg="white")
            label.grid(column=0, row=0)
            tk.mainloop()

    def busca(self, nome):
        """Essa função busca um treino na base de dados"""
        self.nome = nome
        janela_busca = tk.Tk()
        janela_busca.config(bg="#333333")
        janela_busca.title("Sistema de gerenciamento de treinos")
        janela_busca.iconbitmap('gym_86590.ico')

        with open("treinos.json", 'r') as file:
            treinos = json.load(file)

            if not self.nome in treinos.keys():
                texto = "Essa treino não está cadastrado"
                label = tk.Label(janela_busca, text=texto, bg="#333333", fg="white")
                label.grid(column=0, row=0)

            else:
                janela_busca.geometry("600x300")
                texto = f"Treino {self.nome}"
                label = tk.Label(janela_busca, text=texto, bg="#333333", fg="white", font=("Arial", 12))
                label.grid(column=0, row=0)

        tk.mainloop()

    def remove(self, excluir):
        """Essa função remove treinos da base de dados"""
        with open("treinos.json", 'r') as f:
            file = json.load(f)

            del file[excluir]

        with open("treinos.json", 'w') as f:
            json.dump(file, f)

    