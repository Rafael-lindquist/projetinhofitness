import json

class PlanilhaDeExercicio:
    def __init__(self):
        pass

    def cadastrar(self, nome: str, descricao = "sem descricao"):
        """Essa funação cadastra exercícios no
        dataset exercicios.json"""
        self.nome = nome
        self.descricao = descricao
        with open("exercicios.json", 'r') as f:
            file = json.load(f)

        with open("exercicios.json", 'w') as f:
            if self.nome in file.keys():
                print("Esse exercício já está cadastrado")
            else:
                file[self.nome] = descricao
            json.dump(file, f, indent=4)

    def listagem(self):
        """Essa função faz a listagem dos exercícios cadastrados"""
        with open('exercicios.json', 'r') as f:
            print('Esses são os exercícios:\n')
            file = json.load(f)
            for i in file.keys():
                print(i)
            
    def busca(self, ex: str) -> bool:
        self.ex = ex
        """Essa função busca um exercício no dataset
        exercicios.json e retorna True caso o exercicios
        esteja em exercicios.json, senão retorna False"""
        with open("exercicios.json", 'r') as f:
            file = json.load(f)
            for i in file.keys():
                if i == self.ex:
                    print("Exercício já cadastrado")
                
    def excluir(self, ex: str):
        """Essa função remove exercícios do dataset"""
        self.ex = ex
        with open("exercicios.json", 'r') as f:
            file = json.load(f)
        with open("exercicios.json", 'w') as f:
            del file[self.ex]
            json.dump(file, f, indent=4)
            print(f"O exercício {self.ex} foi excluido")
    