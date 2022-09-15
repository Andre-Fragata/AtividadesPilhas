def main():
    pilhaPositivo = []
    pilhaNegativo = []
    resposta = "2"
    while resposta.lower() != "sair":
        resposta = input('Digite um valor para ser armazenado ou sair para terminar:')
        if resposta == "sair":
            print("pilha de números negativos: " ,pilhaNegativo)
            print("pilha de números positivos: ",pilhaPositivo)
            break 
        
        numero = int(resposta)

        if numero >= 0:
            pilhaPositivo.append(resposta)
        else:
            pilhaNegativo.append(resposta)    

main()