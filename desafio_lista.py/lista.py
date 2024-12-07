lista1= []
listapar = []
listaimpar = []
soma = 0

while True:
    recebido = int(input("Digite um número inteiro positivo: \n"))
    if recebido == 0 or recebido < 0:
        break
    else:
        if recebido not in lista1:
         lista1.append(recebido)
         if (recebido % 2) == 0:
            listapar.append(recebido)
            soma = soma + recebido
         else:
            listaimpar.append(recebido)
            soma = soma + recebido
        else:
            print(f"Esse número {recebido} ja foi digitado ")
listaimpar.sort()
listapar.sort()
lista1.sort()
for i in listaimpar:
    print(f"Os números impares digitados são {i}")
for j in listapar:
    print(f"Os números pares digitados são {j}")
for k in lista1:
    print(f"Os números digitados são  {k}")
print(f"A soma dos números é {soma}")