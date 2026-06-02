import random

import Banco

NUMERO_DE_PEDRAS = 32

correspondecias = {
  
'Acido':['HCl', 'HCN','Hl','H2S','HF','H2CrO4', 'Liberam H+ em solução aquosa', 'Geralmente são azedos'], 
                   
'Base':['NH3','Fe(OH)3','Cr(OH)3','Ba(OH)2','Fe(OH)3','Cr(OH)3', 'Liberam íons hidroxila em solução aquosa', 'Geralmente são amargos'],

'Hidreto':['CaH2','H2O'],

'Oxido':['SiO2','TiO','P2O3','CrO3','V2O5'],

'Sal':['Na2CO3','FeCl3','NaBrO4','HClO4','NaCl','Normalmente tem sabor salgado', 'Não são bons condutores de eletricidade, salvo quando estão dissolvidos em água']

}

class Pedra:
  def __init__(self, valores:list):
    self.valor_0 = valores[0]
    self.valor_1 = valores[1]

    self.valor_0_conexao = None
    self.valor_1_conexao = None

    self.pedras_conectadas = []

  def __str__(self):
    return f"({self.valor_0} / {self.valor_1})"

def obter_funcao_elemento(valor:str):
  dicts_keys_list = list(correspondecias.keys())

  if valor in dicts_keys_list:
    return valor
  else:
    for key, array in correspondecias.items():
        if valor in array:
          return key

def e_compativel(valor_a:str, valor_b:str):
  funcao_valor_a = obter_funcao_elemento(valor=valor_a)
  funcao_valor_b = obter_funcao_elemento(valor=valor_b)

  return funcao_valor_a == funcao_valor_b

def deep_e_compativel(pedra_a:Pedra, pedra_b:Pedra):
  valores_pedra_a = [pedra_a.valor_0, pedra_a.valor_1]
  valores_pedra_b = [pedra_b.valor_0, pedra_b.valor_1]

  for val_a in valores_pedra_a:
    for val_b in valores_pedra_b:
      if e_compativel(val_a, val_b):
        return True
  return False
  
def obter_descendente_correspondencias(key:str):
  if key in correspondecias.keys():
    return random.choice(correspondecias[key])
  else:
    raise ValueError(f"Chave {key} inválida para o dicionário correspondencias.")

chance_aparecer_formulas = 0.5
def inicializar_pedra(valores_raw:list):
  valor_0 = valores_raw[0]
  if random.random() <= chance_aparecer_formulas:
    valor_0 = obter_descendente_correspondencias(valor_0)

  valor_1 = valores_raw[1]
  if random.random() <= chance_aparecer_formulas:
    valor_1 = obter_descendente_correspondencias(valor_1)

  espaco_amostral = [valor_0, valor_1]

  valores_cooked = random.sample(espaco_amostral, 2)

  return valores_cooked

def obter_todas_pedras():
  pedra_lista = []

  for id in range(1, NUMERO_DE_PEDRAS + 1):
    pedra_atual = Banco.pegar_valor('pecas', id)

    pedra_processada = inicializar_pedra(pedra_atual)
    
    pedra_lista.append(Pedra(pedra_processada))

  random.shuffle(pedra_lista)

  return pedra_lista

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
