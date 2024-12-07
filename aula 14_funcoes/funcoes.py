#Criando uma função simples
def exibir_programador():
    nome= str(input('digite seu nome:'))
    print(f'seu nome é {nome}')
    
exibir_programador()
#outro exemplo
def exibir_filme():
    #variável local
    nome_filme= str(input('Digite o nome do filme:\n'))
    return nome_filme
print(f'O nome do filme é {exibir_filme()}')

#criar uma função que retorne a soma de 2 numeros digitados pelo usuário

def soma_usuario():
    primeiro_valor=float(input('Digite o primeiro valor: \n'))
    segundo_valor=float(input('Digite o segundo valor: \n'))
    soma= primeiro_valor+segundo_valor
    return soma

print (f'A soma é: {soma_usuario()}')

#função receber parâmetro

def multiplicar_numero(n1,n2):
    return n1*n2
#variaveis globais
quantidade= int(input('Digite a quantidade de produtos comprados: \n'))
valor = float(input('Digite o valor do produto: \n'))
total_compra= multiplicar_numero(quantidade,valor)
print(f'O valor da compra é R${total_compra}')
print(f'O valor da compra é R${multiplicar_numero(quantidade,valor)}')