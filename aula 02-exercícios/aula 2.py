#atividade 1
numero1=float(input('Digite o primeiro número para somar:'))
numero2=float(input('Digite o segundo número para somar:'))
soma= numero1 + numero2 
print ('A soma é igual a '+ str(soma))
#atividade 2
verificar=7
print (f'O tipo da variável é: {type(verificar)}')
#atividade 3
import math
calcular=float(input('Digite um número para calcular: '))
raiz=math.sqrt(calcular)
print (f'Dobro: {calcular*2}\nTriplo: {calcular*3} \nQuadrado: {calcular**2}\nRaiz: {raiz:.3f}')
#atividade 4
calcularNota1=float(input('Digite sua primeira nota: '))
calcularNota2=float(input('Digite sua segunda nota: '))
print (f'sua média é: {(calcularNota1+calcularNota2)/2}')
#atividade 5
carteira=float(input('Informe o valor da sua conta bancaria:'))
print (f'O valor convertido em dólar é: US${carteira/5}')
#atividade extra 1
numeroInt=int(input('Digite um número para elevar ao quadrado: '))
print (f'O quadrado de {numeroInt} é igual a:{numeroInt**2}')
#atividade extra 2
Caracter1=str(input('Digite uma palavra: '))
Caracter2=str(input('Digite mais uma palavra: '))
print (f'O usuário digitou {Caracter1} e {Caracter2}')
#atividade extra 3
numeroPosicao=int(input('Digite um número para saber seu sucessor e antecessor: '))
print(f'O antecessor de {numeroPosicao} é {numeroPosicao-1} e o sucessor de {numeroPosicao} é {numeroPosicao+1}')
#atividade extra 4
altura=int(input('Digite o número da altura para saber o parâmetro e a área do quadrado: '))
base=int(input('Digite o número da base para saber o parâmetro e a área do quadrado: '))
print (f'O parâmetro do quadrado é {altura*2+base*2} e a área é de {altura*base}')
#atividade extra 5
valor=float(input('Digite o valor da prestação: '))
taxa=float(input('Digite o valor da taxa: '))
tempo=int(input('Digite o tempo da prestação: '))
print (f'O valor da prestação é de R${valor*(taxa/100)*tempo}')





