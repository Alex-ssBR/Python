# atividade 2
import random
print('O JOGO COMEÇOU')
comecar = str(input('COMEÇAR? S/N \n')).upper()
if comecar == 'S':
    while True:
        usuario = int(input('CONTINUAR A JOGAR? Sim.1 Não.0\n'))
        if usuario == 1:
            ppt = random.randint(1, 3)
            usuario = int(
                input('Digite um dos números pedra.1 papel.2 tisora.3: \n'))
            if usuario >= 1 and usuario <= 3:
                if usuario == ppt:
                    print('Voces pensaram a mesma coisa ')
                elif usuario == 1 and ppt == 2:
                    print(f'Você perdeu. A máquina jogou papel.{ppt} ')
                elif usuario == 1 and ppt == 3:
                    print(f'Você venceu. A máquina jogou tisora.{ppt} ')
                elif usuario == 2 and ppt == 1:
                    print(f'Você venceu. A máquina jogou pedra.{ppt} ')
                elif usuario == 2 and ppt == 3:
                    print(f'Você perdeu. A máquina jogou tisora.{ppt} ')
                elif usuario == 3 and ppt == 1:
                    print(f'Você perdeu. A máquina jogou pedra.{ppt} ')
                elif usuario == 3 and ppt == 2:
                    print(f'Você perdeu. A máquina jogou papel.{ppt} ')
                else:
                    break
            else:
                print('Apenas de números de 1 a 3')
        elif usuario == 0:
            print('operação finalizada')
            break
else:
    print('Jogue mais vezes')
