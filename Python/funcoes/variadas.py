from time import sleep
import random
from datetime import datetime
def areaRetangular(a, b):
    """
    Retorna a área de um ratângulo com lados iguais aos parâmetros 'a' e 'b'
    """
    return a*b

def escreva(mensagem):
    """
    Escreve a mensagem passada por parâmetro como um título, entre duas linhas
    """
    tam = len(mensagem)
    print('-'*tam)
    print(mensagem)
    print('-'*tam)

def contador(inicio, fim, passo):
    """
    Faz uma contagem de 'inicio' a 'fim' contando de 'passo' em passo
    """
    c = inicio
    if inicio > fim:
        passo = -passo
    while c >= fim:
        print(c, end = ' ')
        sleep(0.5)
        c += passo
    else:
        while c <= fim:
            print(c, end = ' ')
            sleep(0.5)
            c += passo
    print('FIM!')

def maior(lst):
    """
    retorna o maior valor dos números passados por parâmetro em uma lista
    """
    maior = lst[0]
    for c in range(len(lst)):
        if lst[c] > maior:
            maior = lst[c]
    return maior

def menor(lst):
    """
    retorna o menor valor dos números passados por parâmetro em uma lista
    """
    menor = lst[0]
    for c in range(len(lst)):
        if lst[c] < menor:
            menor = lst[c]
    return menor
    
def sorteia(lst):
    """
    retorna uma lista com 5 elementos sorteados da lista passado por parâmetro
    """
    return(random.sample(lst, k=5))
    
def somaPares(lst):
    """
    Retorna o resultado da soma somente dos números pares da lista passada por parâmetro
    """
    soma = 0
    for c in lst:
        if c%2 == 0:
            soma += c
    return soma

def voto(ano):
    """
    Retorna a situação de voto do ano de nascimento passado por parâmetro
    """
    idade = datetime.now().year - ano
    if idade > 18 and idade < 70:
        return f'com {idade} anos voto: OBRIGATÓRIO'
    elif idade < 16:
        return f'com {idade} anos voto: NEGADO'
    else:
        return f'com {idade} anos voto: OPCIONAL'

def fatorial(num=1, show=False):
    """
    Escreve na tela o fatorial do 'num' passado por parâmetro e mostra o processo caso 'show' receba True.
    """
    if show == False:
        fatorial = c = 1
        while c < num:
            fatorial *= (c+1)
            c += 1
        print(f'O fatorial de {num} é = {fatorial}')
    else:
        fatorial = c = 1
        while c < num:
            print(f'{c}x', end='')
            fatorial *= (c+1)
            c += 1
        print(f'{c}={fatorial}')

def ficha(nome='', gols=0):
    """
    Recebe o nome e quantos gols um jogador fez e mostra de forma formatada
    """
    if nome == '':
        return f' O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

def notas(lst, sit=False):
    d = dict()
    d['Quantidade de nota'] = len(lst)
    d['Maior nota'] = max(lst)
    d['Menor nota'] = min(lst)
    d['Média'] = round((sum(lst)/len(lst)), 2)
    if d['Média'] >= 7:
        situacao = 'Boa'
    else:
        situacao = 'Ruim'
    if sit == True:
        d['situação'] = situacao
    return d
def media(lst):
    """
    Retorna a média dos números da lista passada por parâmetro
    """
    m = 0
    for c in range(len(lst)):
        m += lst[c]
    return m/len(lst)
    
def Pyhelp():
    while True:
        msg = str(input('Digite uma função ou biblioteca: '))
        if msg.upper() == 'FIM':
            print('Até logo')
            break
        else:
            help(msg)
