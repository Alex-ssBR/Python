lista2 = []

while True:
    digitado = input("Digite um número (ou 'sair' para encerrar): \n")

    if digitado.lower() == 'sair':
        break  

    try:
        num = int(digitado)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue  

    
    if num not in lista2:
        lista2.append(num)
    else:
        print("Esse número já foi digitado.")

lista2.sort()
print("Valores únicos digitados, em ordem crescente:", lista2)
