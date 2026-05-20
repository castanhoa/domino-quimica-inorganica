import matplotlib.pyplot as plt
import Banco.py
import Professor
def dados_alunos(p: Professor):
    #Joao cria a interface para receber o dado que será usado de parametro, preferencia seleção de lista
    dado_determinante = input()
    sala = p.turmas
    conjunto = dados_alunos(dado_determinante, sala)
    nome = []
    partidas = []
    tempo = []
    for i in range(len(conjunto)):
        nome.append(conjunto[i][0])
        partidas.append(conjunto[i][1])
        tempo.append(conjunto[i][2])
    ax = plt.subplots(figsize=(6, 4))
    if dado_determinante == 'número de partidas':
        ax.bar(nome, partidas, color = 'blue')
    elif dado_determinante == 'Tempo de jogo':
        ax.bar(nome, tempo, color ='red')
    plt.tight_layout()
    plt.show()