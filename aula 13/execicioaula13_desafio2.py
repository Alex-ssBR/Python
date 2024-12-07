#desafio 2
maior=0
import random
jogador1=(input('Coloque seu nome: \n'))
jogador1_random= random.randint(1,6)
print(jogador1_random)
jogador2= (input('Coloque seu nome: \n'))
jogador2_random= random.randint(1,6)
print(jogador2_random)
jogador3= (input('Coloque seu nome: \n'))
jogador3_random= random.randint(1,6)
print(jogador3_random)
jogador4= (input('Coloque seu nome: \n'))
jogador4_random= random.randint(1,6)
print(jogador4_random)
jogadores={
    jogador1 : jogador1_random,
    jogador2 : jogador2_random,
    jogador3 : jogador3_random,
    jogador4 : jogador4_random
    }
for i,j in jogadores.items():
    if maior < j:
        maior = j
        aluno_maior= i
print(f' {aluno_maior} tem o maior número, elx pegou {maior}')        
      
