import random
import Banco
NUMERO_DE_PEDRAS = 32
correspondecias = { 'Acido':['HCN','Hl','H2S','HF','H2CrO4'], 
'Base':['Fe(OH)3','Cr(OH)3','Ba(OH)2','Fe(OH)3','Cr(OH)3'],
'Hidreto':['NH3','CaH2','HCl','H2O','CaH2'],
'Oxido':['SiO2','TiO','P2O3','CrO3','V2O5'],
'Sal':['Na2CO3','FeCl3','NaBrO4','HClO4','NaCl']}

possibilidades = [
['Sal', 'Na2CO3'],
['Oxido', 'Sal'],
['Oxido', 'SiO2'],
['Oxido', 'Base'],
['Base', "Cr(OH)3"],
['Base', 'Fe(OH)3'],
['Acido', 'Base'],
['Acido', 'HCN'],
['Acido', 'Hidreto'],
['Hidreto', 'CaH2'],
['Hidreto', 'NH3'],
['Hidreto', 'HCl'],
['Oxido', 'Hidreto'],
['Oxido', 'TiO'],

]

len_possibilidades = len(possibilidades)

class Pedra:
  def __init__(self, valores:list):
    self.valor_0 = valores[0]
    self.valor_1 = valores[1]

    self.valor_0_conexao = None
    self.valor_1_conexao = None

    self.pedras_conectadas = []

def obter_funcao_elemento(valor:str):
  dicts_keys_list = list(correspondecias.keys())

  if valor in dicts_keys_list:
    return valor
  else:
    for key, array in correspondecias.items():
      for elemento in array:
        if elemento == valor:
          return key

def e_compativel(valor_a:str, valor_b:str):
  funcao_valor_a = obter_funcao_elemento(valor=valor_a)
  funcao_valor_b = obter_funcao_elemento(valor=valor_b)

  if funcao_valor_a == funcao_valor_b:
    return True
  else:
   return False


def obter_todas_pedras(quantia:int):
  pedra_lista = []
  for id in range(1, NUMERO_DE_PEDRAS + 1):
    pedra_atual = Banco.pegar_valor('pecas', id)
    pedra_lista.append(Pedra(pedra_atual))
  random.shuffle(pedra_lista)
  return pedra_lista
  # possibilidades_atual = possibilidades.copy()

  # if quantia > len_possibilidades:
  #   delta = quantia - len_possibilidades
  #   for _ in range(delta):
  #     possibilidades_atual.append(random.choice(possibilidades))

  # pedras_lista = []

  # padras_valores = random.sample(possibilidades, quantia)

  # for indice in range(quantia):
  #   pedras_lista.append(Pedra(padras_valores[indice]))

  # return pedras_lista



# 
#   def forma(self):
#     for n in range(2):
#       chance = random.randint(1, 100)
#       #escolhe como a peça será mostrada,ainda falta atribuir às peças diretamente aos arquivos de imagem
#       #Formulas aleatórias
#       if chance <= probabilidadeFormula
#         match self.valor[n]:
#           case 'acido':
#             random.choice(formulasAcidos)
#           case 'basico':
#             random.choice(formulasBases)
#           case 'sal':
#             random.choice(formulasSais)
#           case 'oxido':
#             random.choice(formulasOxidos)
#       elif chance <= probabilidadeFormula + probabilidadeConceito:
#       #falta adicionar o código pega a parte da peça com conceito
#         match self.valor[n]:
#           case 'acido':
#           case 'basico':
#           case 'sal':
#           case 'oxido':
#        #propriedades     
#       else:
#         match self.valor[n]:
#           case 'acido':
#             random.choice(propriedadesAcidos)
#           case 'basico':
#             random.choice(propriedadesBases)
#           case 'sal':
#             random.choice(propriedadesSais)
#           case 'oxido':
#             random.choice(propriedadesOxidos)
