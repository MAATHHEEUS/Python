import random
class jokenpo:
    usuario = str(input('escolha entre pedra, papel ou tesoura! '))
    #algum codigo de verificação
    lista = ['pedra', 'papel', 'tesoura']
    computador = random.choice(lista)
    #bloco da tesoura
    if usuario == 'tesoura' and computador == 'papel':
        print('você ganhou!')
    elif usuario == 'tesoura' and computador == 'pedra':
        print('você perdeu')
    elif usuario == 'tesoura' == computador:
        print('deu empate')

    #bloco do papel
    if usuario == 'papel' and computador == 'pedra':
        print('você ganhou!')
    elif usuario == 'papel' and computador == 'tesoura':
        print('você perdeu')
    elif usuario == 'papel' == computador:
        print('deu empate')

    #bloco da pedra
    if usuario == 'pedra' and computador == 'tesoura':
        print('você ganhou!')
    elif usuario == 'tesoura' and computador == 'papel':
        print('você perdeu')
    elif usuario == 'tesoura' == computador:
        print('deu empate')
