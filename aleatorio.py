# gerar número aleatório
# from random import randint
# numero_aleatorio = randint(0, 10)
# print(numero_aleatorio)

# Atividade 1
from random import randint
usuario = int(input('Digite um número aleatório: '))
maquina = randint(0, 5)
if usuario == maquina:
    print(f'o número: {maquina}')
    print('você acertou o número')
else:
    print(f'o número: {maquina}')
    print('você errou o número')
# Atividade 2
velocidade = float(input('Digite a velocidade em que você estava: '))
if velocidade > 80:
    print(
        f'Você foi multado. estava em {velocidade}km/h\nmulta: {(velocidade-80)*7}')
else:
    print(f'Você não foi multado. estava em {velocidade}h')
# Atividade 3
viagem = float(input('Digite a distância que você percorreu: '))
if viagem <= 200:
    print(f'Preço da passagem: R${viagem*0.50}')
else:
    print(f'Preço da passagem: R${viagem*0.45}')
# Atividade 4
#exemplo do professor 1
numero1= int(input('Digite o primeiro número'))
numero2= int(input('Digite o segundo número'))
numero3= int(input('Digite o terceiro número'))


num1 = float(input('primeiro número: '))
num2 = float (input('segundo número: '))
num3 = float (input('terceiro número: '))
if num1 <= num2 and num1 <= num3:
    print(f'{num1} é o menor número')
elif num1 >= num2 and num1 >= num3:
    print(f'{num1} é o maior número')
if num2 <= num1 and num2 <= num3:
    print(f'{num2} é o menor número')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} é o maior número')
if num3 <= num1 and num3 <= num2:
    print(f'{num3} é o menor número')
elif num3 >= num1 and num3 >= num2:
    print(f'{num3} é o maior número')
else:
    print('Todos são iguais')
# maior = max(num1, num2, num3)/ menor = min(num1, num2, num3)
# Atividade 5
trianguloa = int(input('primeiro reta: '))
triangulob = int(input('segunda reta: '))
trianguloc = int(input('terceira reta: '))
if trianguloa + triangulob > trianguloc and trianguloa + trianguloc > triangulob and triangulob+trianguloc > trianguloa:
    print('Sim, podem formar um triângulo.')
else:
    print('Não, não podem formar um triângulo.')
    