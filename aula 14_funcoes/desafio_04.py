val1_usuario=float(input('valor 1: \n'))
val2_usuario=float(input('valor 2: \n'))
val3_usuario=float(input('valor 3: \n'))
def maior(val1,val2,val3):
    maior_valor= max(val1,val2,val3)
    return maior_valor
print(f'O MAIOR VALOR É: {maior(val1_usuario,val2_usuario,val3_usuario)}')

