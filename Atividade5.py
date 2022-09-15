estacionamento = []
numVagas = 5


def main():
    operation = 1
    while operation != 0:
        print ("Carros no Estacionamento",estacionamento)

        operation = int(input("Digite [1] para entrada; [2] para saida; [0]Finalizar"))
        
        if operation == 1:
            entrada()
        elif operation == 2:
            saida()
        else:
            operation == 0

def entrada():
    global estacionamento, numVagas
    numVagasOff = len(estacionamento)
    numVagasOn = numVagas - numVagasOff

    if numVagasOn > 0:
        entradacarro = str(input("Digite o Nome do carro:"))
        estacionamento.append(entradacarro)
        print ("\n\n")
        print ("Entrada",entradacarro)
        print ("\n\n")
    elif numVagasOn == 0:
        print ("\n\n")
        print("Vagas Indisponível")
        print ("\n\n")
def saida():
    global estacionamento, numVagas
    numVagasOff = len(estacionamento)
    ultimo = numVagasOff-1
    print ("\n\n")
    print ("Saída",estacionamento[ultimo])
    print ("\n\n")
    estacionamento.pop()
main()