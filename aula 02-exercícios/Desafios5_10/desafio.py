#desafio 3
cont=0
soma=0
while cont<500:
    if cont%2!=0 and cont%3 == 0:
        soma+=cont
        cont+=1
print(soma)
