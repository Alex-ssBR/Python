# valores = []

# for i in range(5):
#     num = int(input(f"Digite o {i+1}° valor: "))

#     posicao = 0
#     while posicao < len(valores) and valores[posicao] < num:
#         posicao += 1

#     valores.insert(posicao, num)

# print("Lista ordenada:", valores)

# desafio 3 do prof
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
