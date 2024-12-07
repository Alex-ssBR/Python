salario=float(input('Informe seu salário:'))
salarioComAumento=0
if (salario<2000):
    salarioComAumento= (f'Seu salário atual = {salario+ (salario*0.15)}')
    print(salarioComAumento)
elif (salario<3000 and salario>=2000):
    salarioComAumento= (f'Seu salário atual = {salario+ (salario*0.10)}')
    print(salarioComAumento)
else: 
    (salario>=3000)
    salarioComAumento= (f'Seu salário atual = {salario+ (salario*0.05)}')
    print(salarioComAumento)    
    