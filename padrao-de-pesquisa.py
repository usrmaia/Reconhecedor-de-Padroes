class Padrao():
  def __init__(self, padrao, texto):
    self.padrao = padrao
    self.texto = texto

  # TODO só falta fazer a mesma coisa só que com automato, só
  def Pesquisar(self, padrao, texto):
    if not texto:
      if not padrao: return 1
      return 0
    if not padrao: return 1 + self.Pesquisar(self.padrao, texto)

    if padrao[0] == texto[0]: return self.Pesquisar(padrao[1:], texto[1:])
    return self.Pesquisar(padrao, texto[1:])

if __name__ == "__main__":
  padrao = ""
  texto = ""
  p = Padrao(padrao, texto)
  print(p.Pesquisar(padrao, texto))