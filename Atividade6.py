frase = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(frase):
    if frase[x] == "(":
        pilha.append("(")
    if frase[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")