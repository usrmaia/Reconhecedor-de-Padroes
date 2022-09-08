class Padrao():
  def __init__(self):
    self.padrao = ""
    self.texto = ""

  def setPadrao(self, padrao):
    self.padrao = padrao
  
  def setTexto(self, texto):
    self.texto = texto

  # TODO só falta fazer a mesma coisa só que com automato, só
  def Pesquisar(self, padrao, texto):
    if not texto:
      if not padrao: 
        self.printIndice(texto)
        return 1
      return 0
    if not padrao: 
      self.printIndice(texto) 
      lt = len(self.texto) - len(texto) - len(self.padrao) + 1
      texto = self.texto[lt:]
      return 1 + self.Pesquisar(self.padrao, texto)

    if padrao[0] == texto[0]: return self.Pesquisar(padrao[1:], texto[1:])
    return self.Pesquisar(padrao, texto[1:])
  
  def printIndice(self, texto): 
    n = len(self.texto) - len(texto) - len(self.padrao)
    print(f"Padrão encontrado no índice {n}")
    pass

def Pesquisar(padrao, texto, padrao_f, texto_f):
  if not texto:
    if not padrao: 
      return 1
    return 0
  if not padrao: 
    return 1 + Pesquisar(padrao_f, texto, padrao_f, texto_f)

  if padrao[0] == texto[0]: return Pesquisar(padrao[1:], texto[1:], padrao_f, texto_f)
  return Pesquisar(padrao, texto[1:], padrao_f, texto_f)