valores = []
for i in range(5):
    valor = float(input(f'Digite o valor {i + 1}: '))
    valores.append(valor)

maior_valor = max(valores)
menor_valor = min(valores)

posicoes_maior = [i for i, v in enumerate(valores) if v == maior_valor]
posicoes_menor = [i for i, v in enumerate(valores) if v == menor_valor]

print(f'O maior valor digitado foi {maior_valor} nas posições: {posicoes_maior}')
print(f'O menor valor digitado foi {menor_valor} nas posições: {posicoes_menor}')