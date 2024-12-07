produtos= {
    "arroz": 20,
    'feijao': 8,
    'oleo': 7,
    "macarrao": 4,
    'sabonete': 2,
    
    }
#exibir elegantemente minha lista
for prod,preco in produtos.items():
    print(f'O {prod} está no valor R${preco}')
#verificar se há molho de tomate na lista________________________________________
# for prod,preco in produtos.items():
#     if "molho de tomate" in prod:
#         print(f'Tem molho sim! O {prod} está R${preco}')
#     else:
#         print(' Não tem molho de tomate!')
if 'molho de tomate' in produtos:
    for prod,preco in produtos.items():    
        if 'molho de tomate' in prod:
            print(f'O preço do molho de tomate é R${preco}')
else:
    print('não temos')
#adicionar um novo produto na lista________________________________________
produtos['molho de tomate']=2   
if 'molho de tomate' in produtos:
    for prod,preco in produtos.items():    
        if 'molho de tomate' in prod:
            print(f'O preço do molho de tomate é R${preco}')
else:
    print('não temos')
