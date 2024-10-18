from exercicios import PlanilhaDeExercicio
from planilha import Planilha

criarplanilha = input("Deseja criar uma planilha? [S/N] : ")
if criarplanilha == 'S':
    ativado = True
    inst1 = Planilha()
    instancia1 = PlanilhaDeExercicio()
    inst1.menu()
else:
    print('Ok')
    ativado = False

while ativado:
    resposta = int(input("Digite um número: "))
    if resposta == 1:
        exercicio = input("Qual o exercício: ")
        descricao = input("Qual a descrição do exercício: ")
        instancia1.cadastrar(exercicio, descricao)
    
    elif resposta == 2:
        excluir = input("Qual exercício excluir: ")
        instancia1.excluir(excluir)

    elif resposta == 3:
        instancia1.listagem()

    elif resposta == 4:
        buscar = input("Qual exercício buscar: ")
        instancia1.busca(buscar)
    
    interromper = input("Dejesa fazer mais alguma ação na planilha? [S/N] : ")
    if interromper != "S":
        break

print("Sua planilha de treino está pronta!")