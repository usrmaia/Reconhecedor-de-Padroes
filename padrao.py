class Padrao():
  def __init__(self):
    self.padrao = ""
    self.texto = ""

  def ForcaBruta(self, padrao, texto):
    if not texto:
      if not padrao: 
        self.printIndice(texto)
        return 1
      return 0
    elif not padrao: 
      self.printIndice(texto) 
      return 1 + self.ForcaBruta(self.padrao, texto)

    if padrao[0] == texto[0]: return self.ForcaBruta(padrao[1:], texto[1:])
    else: return self.ForcaBruta(self.padrao, texto[1:])
  
  def KMP(self):
    P = self.padrao
    T = self.texto
    # Compute the start position (number of chars) of the longest suffix that matches a prefix,
    # and store them into list K, the first element of K is set to be -1, the second
    #
    K = []  # K[t] store the value that when mismatch happens at t, should move Pattern P K[t] characters ahead
    t = -1  # K's length is len(P) + 1, the first element is set to be -1, corresponding to no elements in P.
    K.append(t)  # Add the first element, keep t = -1.
    for k in range(1, len(P) + 1):
        # traverse all the elemtn in P, calculate the corresponding value for each element.
        while(t >= 0 and P[t] != P[k - 1]):  # if t=-1, then let t = 0, if t>=0 and current suffix doesn't match, then try a shorter suffix
            t = K[t]
        t = t + 1  # If it matches, then the matching position should be one character ahead.
        K.append(t)  # record the matching postion for k
    #print(K)

    # Match the String T with P
    m = 0  # Record the current matching position in P when compared with T
    for i in range(0, len(T)):  # traverse T one-by-one
        while (m >= 0 and P[m] != T[i]):  # if mismatch happens at position m, move P forward with K[m] characters and restart comparison
            m = K[m]
        m = m + 1  # if position m matches, move P forward to next position
        if m == len(P):  # if m is already the end of K (or P), the a fully match is found. Continue comparison by move P forward K[m] characters
            # print (i - m + 1, i)
            self.printIndice(self.texto[i + 1:])
            m = 0
    
  def printIndice(self, texto): 
    fim = len(self.texto) - len(texto) - 1
    inicio = fim - len(self.padrao) + 1
    print(f"Padrão encontrado no índice {inicio}-{fim}")
    pass

  def setPadrao(self, padrao):
    self.padrao = padrao
  
  def setTexto(self, texto):
    self.texto = texto