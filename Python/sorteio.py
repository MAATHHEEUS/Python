#comentário
import math
import random
class sorteio:
    nome = str(input('qual seu nome? '))
    print('olá '+nome+', prazer em te conhecer!!')
    nome1 = input('digite o nome do primeiro aluno')
    nome2 = input('digite o nome do segundo aluno')
    nome3 = input('digite o nome do terceiro aluno')
    nome4 = input('digite o quarto aluno')
    lista = [nome1, nome2, nome3, nome4]
    sorteio = random.choice(lista)
    print('o aluno sorteado foi {}.'.format(sorteio))
