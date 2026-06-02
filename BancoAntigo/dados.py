import matplotlib.pyplot as plt
import Banco.py
import Professor
def dados_alunos(p: Professor):
    #Joao cria a interface para receber o dado que será usado de parametro, preferencia seleção de lista
    dado_determinante = input()
    sala = p.turmas
    conjunto = Banco.pegar_dados_alunos(dado_determinante, sala)
    nome = []
    partidas = []
    tempo = []
    for i in range(len(conjunto)):
        nome.append(conjunto[i][0])
        partidas.append(conjunto[i][1])     
    ax = plt.subplots(figsize=(6, 4))
    ax.bar(nome, partidas, color = 'blue')
    plt.show()