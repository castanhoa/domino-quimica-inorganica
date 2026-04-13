import random
class Peca:
  valor = []
  local = 0
# 0 = monte, 1 = mão do jogador 1, 2 = mão da IA
  dupla = False
  def forma(valor):
    if valor[0] == valor [1]:
      dupla == True
    for n in len(valor):  
      match valor[n]:
        case 'acido': 
          random.choise(listaDeAcidos.)
        case 'basico':
          random.choise(listaDeBases)
        case 'sal':
          random.choise(listaDeSais)
        case 'oxido':
          random.choise(listaDeOxidos)
