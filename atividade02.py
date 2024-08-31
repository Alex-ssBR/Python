#desafio 01
name=str(input("Coloque seu nome: "))
name='alex silva santos'
print(f'Tudo maiúsculo: {name.upper()}')
print(f'Tudo minúsculo: {name.lower()}')
noempty=name.replace(' ', '')
print(f'Quantas letras: {len(noempty)}')
print(f'Primeira letra: {name[:1]}')

#desafio 02
cidade=str(input("Digite o nome da cidade: ")).capitalize()
santos_=cidade.split()

if santos_[0]=="Santos":   
    print(f'{cidade} começa com Santos')
else:
    print(f'{cidade} não começa com Santos')
#desafio 03
name=str(input("Coloque seu nome: "))
print(f'Tem silva no seu nome {"Silva" in name}')

#desafio 04
name_=str(input("Coloque uma frase: "))
A=name_.count('A')
print(f'{A} quantidades de as')
position='A'
print(f'{name_.find(position)}')
print(f'{name_.rfind(position)}')

#desafio 05
name_=str(input("Coloque seu nome: "))
nameseparate=name_.split()
print(f'primeira nome é {nameseparate[0]}\ne último nome é {nameseparate[-1]}')



