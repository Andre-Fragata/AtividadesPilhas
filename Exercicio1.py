
def main():

    pilha = []

    while True:

        palavra = input("Digite uma palavra para empilhar ou \n -> #desempilha, para ver a última \n -> #tamanho, para ver o tamanho \n -> #fim, para finalizar \n")

        if palavra.lower() == "#fim":
            print("Programa finalizado, a pilha final é: ", pilha)
            break
        elif palavra.lower() == "#desempilha":
            print("Elemento", desempilhar(pilha), "desempilhado com sucesso.")
        elif palavra.lower() == "#tamanho":
            verTamanhoPilha(pilha)
        else:
            empilhar(palavra, pilha)
            print("Elemento", palavra, "empilhado com sucesso.")
        print()


def empilhar(elemento, pilha):
    pilha.append(elemento)

def desempilhar(pilha):
    return pilha.pop()

def verTamanhoPilha(pilha):
    print("A pilha possui", len(pilha), "elementos")


#execute
main()
    