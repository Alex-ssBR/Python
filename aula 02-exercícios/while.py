#exibir os números ímpares 100-150
numero=100
while numero<150:
    if numero% 2 != 0:
        print(numero)
    numero+=1
#resolução 2
cont=101
while True:
    print(cont)
    if cont>150:
        break
    cont+=2
#resolução 3
cont=101
while cont<150:
    print(cont)
    cont+=2