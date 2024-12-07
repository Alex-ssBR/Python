#desafio 1
aluno=str(input('Digite seu nome: \n'))
nota=float(input('Digite sua nota: \n'))
dados= { aluno: nota}
if nota in dados.keys() < 6:
        print(f'Você reprovou. Sua nota: {nota}')
else:
        print(f'Você passou. Sua nota: {nota}')
print(dados)
