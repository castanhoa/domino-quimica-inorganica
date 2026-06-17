from Banco import pegar_dados_alunos
import matplotlib.pyplot as plt
## faça o professor escolher entre ver como lista ou grafico
lista = pegar_dados_alunos(dado, id_turma)
if escolha = 'grafico':
##faça uma seleção entre tempo de jogo, vitorias, e partidas e associe à variavel
##também permita que o professor selecione o id da turma

    
    data = []
    for i in lista:
        data.append(lista[i][1])
    plt.hist(data, bins=6)
    plt.grid()
    plt.title(f"distribuição de {dado}")
    plt.show()
elif escolha = 'lista'