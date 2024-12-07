nome=input('Digite um nome para ve-lo ao contrário: \n')
print(len(nome))
#_____________________________________________
nomeinvertido= nome[::-1]
print(nomeinvertido)
#_____________________________________________
nomeinvertido2=''.join(reversed(nome))
print(nomeinvertido2)
#_____________________________________________
cont=1
while True:
    if cont==len(nome)+1:
        break
    print(nome[len(nome)- cont])
    cont=cont+1
#_____________________________________________
desen=input('Digite seu nome: \n')
contCar=len(desen)
while contCar>0:
    inicio=contCar-1
    print(desen[inicio])
    contCar-=1