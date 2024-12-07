valores = []

for i in range(5):
    num = int(input(f"Digite o {i+1}° valor: "))
    
    posicao = 0
    while posicao < len(valores) and valores[posicao] < n:
        posicao += 1
    
    valores.insert(posicao, num)

print("Lista ordenada:", valores)
