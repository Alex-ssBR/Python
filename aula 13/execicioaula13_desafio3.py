listaDicionario=[]
dicionario={}
listaMulheres=[]
listaMaiorMedia=[]
quantidadeP=0
somaI=0
mediaI=0
while True:
    nome=str(input('Digite seu nome: \n'))
    sexo=str(input('Digite seu sexo[M/F]: \n')).upper()
    if sexo == 'F':
        listaMulheres.append(nome)
        idade=int(input('Digite sua idade: \n'))
        somaI+=idade
    #adicionar dados no dicionário
        dicionario['nome']=nome
        dicionario['sexo']=sexo
        dicionario['idade']=idade
        listaDicionario.append(dicionario)
    else:
        idade=int(input('Digite sua idade: \n'))
        somaI+=idade
    #adicionar dados no dicionário
        dicionario['nome']=nome
        dicionario['sexo']=sexo
        dicionario['idade']=idade
        listaDicionario.append(dicionario.copy())
        
    quantidadeP+=1
    valor= int(input('Digite 1 para continuar. Digite 0 para cancelar \n'))
    if valor == 0:
        break
    else:
        continue
mediaI= somaI/quantidadeP
if idade > mediaI:
    listaMaiorMedia.append(nome)
        

print(f'{quantidadeP} pessoas foram cadastradas.\n A média é:\n {somaI/quantidadeP}\n Lista de mulheres: \n{listaMulheres} \n Lista de maior da média: \n {listaMaiorMedia}')