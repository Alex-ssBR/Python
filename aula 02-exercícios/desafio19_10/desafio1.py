# desafio 1 ____________________________________
maiorNum = -10000
menorNum = 100000
media = 0
for i in range(10):
    numeros = int(input('Digite um número: \n'))
    media += numeros
    if numeros < menorNum:
        menorNum = numeros
    if numeros > maiorNum:
        maiorNum = numeros
print(
    f'O maior número é {maiorNum} e o menor número é {menorNum}.\nMédia:{media/10}')
