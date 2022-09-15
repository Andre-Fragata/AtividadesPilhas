import random

class Pilha():

    def __init__(self):
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
    
    def tamanho(self):
        return len(self.pilha)

    def ultimo(self):
        i = self.tamanho() - 1
        return self.pilha[i]
    
    def print(self):
        print(self.pilha)

def main():
    pilha1 = Pilha()
    pilha2 = Pilha()

    popularPilha(pilha1, pilha2)

    pilha1.print()
    pilha2.print()

    desempilhar(pilha1, pilha2)


def desempilhar(pilha1, pilha2):
    for i in range(0, pilha1.tamanho()):
        numero = pilha1.desempilha()
        if numero == pilha2.desempilha():
            print("As pilhas possuíam o número", numero, "iguais na posição ", i)


def popularPilha(pilha1, pilha2):
    i = 0
    for i in range(0, 20):
        aleatorio = random.randint(1,5)
        if i % 2 == 0:
            pilha1.empilha(aleatorio)
        else:
            pilha2.empilha(aleatorio)


#execute
main()