class Pilha():

    def _init_(self):
        self.pilha = []

    def estaVazia(self):
        if len(self.pilha) == 0:
            return True
        else:
            return False

    def empilha(self, elemento):
        self.pilha.append(elemento)

    def desempilha(self):
        if not self.estaVazia():
            elemento = self.pilha.pop()
            return elemento        
    

    def getPilha(self):
        saida =  ''
        return saida.format(self.pilha)



def main():
    pilhaDePalavras = Pilha()
    desempilhadas = Pilha()
    fim = False
    while not fim:
        palavra = input('Informe uma palavra ')

        if palavra == 'stop':
            fim = True
        elif palavra == 'ctrl+z':
            elemento = pilhaDePalavras.desempilha()
            desempilhadas.empilha(elemento)
            print(desempilhadas)
        elif palavra == 'ctrl+y':
            elemento = desempilhadas.desempilha()
            pilhaDePalavras.empilha(elemento)
            print(pilhaDePalavras)
        else:
            pilhaDePalavras.empilha(palavra)

main()