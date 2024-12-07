#declarar a tupla
lanches = ('misto','beirute','bauru','coxinha')

#exibindo uma tupla 
print(lanches)


#exibir elegantemente
for lan in lanches:
    print(lan)
    print(10 * "_")
    

    
    
    
#diferença da lisa nao da pra adicionar ou remover na tupla

#apenas convertendo tuplas em lista consigo adicionar ou remover 
listaLanches = list(lanches)

#exibir a lista 
for li in listaLanches:
    print(li)
    print(10 * "*")
    
    
#adicionar mais um lanche 
listaLanches.append('x-mortal')

#conveter a lista em tupla 
novoLanches = tuple(listaLanches)

#exibir elegantemente a nova tupla
for novoLa in novoLanches:
    print(novoLa)