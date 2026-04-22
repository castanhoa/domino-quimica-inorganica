import random
<<<<<<< HEAD
=======
class Peca:
  def __init__(self, valor1: str, valor2: str):
    self.valor = [valor1, valor2]
    self.local = 0
# 0 = monte, 1 = mão do jogador 1, 2 = mão da IA
    if valor1 == valor2:
      self.dupla =  True
    else:
      self.dupla = False
  def forma(self):
    for n in range(2):
      chance = random.randint(1, 100)
      #escolhe como a peça será mostrada,ainda falta atribuir às peças diretamente aos arquivos de imagem
      #Formulas aleatórias
      if chance <= probabilidadeFormula:
        match self.valor[n]:
          case 'acido':
            random.choice(formulasAcidos)
          case 'basico':
            random.choice(formulasBases)
          case 'sal':
            random.choice(formulasSais)
          case 'oxido':
            random.choice(formulasOxidos)
      elif chance <= probabilidadeFormula + probabilidadeConceito:
      #falta adicionar o código pega a parte da peça com conceito
        match self.valor[n]:
          case 'acido':
            pass
          case 'basico':
            pass
          case 'sal':
            pass
          case 'oxido':
            pass
       #propriedades     
      else:
        match self.valor[n]:
          case 'acido':
            random.choice(propriedadesAcidos)
          case 'basico':
            random.choice(propriedadesBases)
          case 'sal':
            random.choice(propriedadesSais)
          case 'oxido':
            random.choice(propriedadesOxidos)
>>>>>>> 6efdb5a795f212df7330d76dcf8d42ee2a5e97af

correspondecias = { 'Acido':['HCN','Hl','H2S','HF','H2CrO4'], 
'Base':['Fe(OH)3','Cr(OH)3','Ba(OH)2','Fe(OH)3','Cr(OH)3'],
'Hidreto':['NH3','CaH2','HCl','H2O','CaH2'],
'Oxido':['SiO2','TiO','P2O3','CrO3','V2O5'],
'Sal':['Na2CO3','FeCl3','NaBrO4','HClO4','NaCl']}

def get_key(my_dict, search_value):
  for key, value in my_dict.items():
      if value == search_value:
          return key

class Pedra:
  def __init__(self):
    self.elemento_0 = random.choice()

    self.elemento_1 = 




#   def __init__(self, valor1: str, valor2: str)
#     self.valor = [valor1, valor2]
#     self.local = 0
# # 0 = monte, 1 = mão do jogador 1, 2 = mão da IA
#     if valor1 == valor2:
#       self.dupla =  True
#     else:
#       self.dupla = False
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
