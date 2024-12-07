# desafio 2 ____________________________________
mediaH = 0
mediaM = 0
for i in range(10):
    idade = int(input('Digite sua idade:\n'))
    sexo = str(input('Digite seu sexo [M:F]:\n')).upper()
    if sexo == 'M':
        mediaH += idade
    elif sexo == 'F':
        mediaM += idade
    else:
        print('INVÁLIDO\n Repita')
        i -= 1
print(
    f'A média das mulheres é {mediaM/10} e a média dos homens é {mediaH/10}.\nMédia: {(mediaH+mediaM)/10}')
