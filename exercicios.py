import json
import tkinter as tk

class PlanilhaDeExercicio:

    def cadastrar(self, nome: str, descricao = "sem descricao"):
        """Essa funação cadastra exercícios no
        dataset exercicios.json"""
        self.nome = nome
        self.descricao = descricao
        with open("exercicios.json", 'r', encoding='utf8') as f:
            file = json.load(f)

        with open("exercicios.json", 'w', encoding='utf8') as f:
            if self.nome in file.keys():
                pass
            else:
                file[self.nome] = descricao
                json.dump(file, f, indent=4)

    def listagem(self):
        """Essa função faz a listagem dos exercícios cadastrados"""
        with open('exercicios.json', 'r', encoding='utf8') as f:
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
                
    def busca(self, ex: str) -> bool:
        self.ex = ex
        """Essa função busca um exercício no dataset
        exercicios.json e retorna True caso o exercicios
        esteja em exercicios.json, senão retorna False"""
        with open("exercicios.json", 'r', encoding='utf8') as f:
            file = json.load(f)
            janela_listagem = tk.Tk()
            janela_listagem.config(bg="#333333")
            janela_listagem.title("Sistema de gerenciamento de treinos")
            janela_listagem.iconbitmap('gym_86590.ico')
            if self.ex in file.keys():
                texto = f"Exercício já cadastrado: {self.ex} - {file[self.ex]}"
            else: 
                texto = "Exercício não cadastrado"
            label = tk.Label(janela_listagem, text=texto, bg="#333333", fg="white")
            label.grid(column=0, row=0)
            tk.mainloop()
                
    def excluir(self, ex: str):
        """Essa função remove exercícios do dataset"""
        self.ex = ex
        with open("exercicios.json", 'r', encoding='utf8') as f:
            file = json.load(f)
        with open("exercicios.json", 'w', encoding='utf8') as f:
            del file[self.ex]
            json.dump(file, f, indent=4)

    def atualizar(self, ex:str, descricao: str):
        """Essa função atualiza um exercícios"""
        self.ex = ex
        self.descricao = descricao
        with open("exercicios.json", 'r', encoding='utf8') as f:
            file = json.load(f)

        del file[self.ex]
        file[self.ex] = self.descricao

        with open("exercicios.json", 'w', encoding='utf8') as f:
            json.dump(file, f, indent=4)


    