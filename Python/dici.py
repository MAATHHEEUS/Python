from random import randint
from time import sleep
from operator import itemgetter
from datetime import datetime
class dic:
    pessoas = dict()
    conjunto = []
    mulheres = []
    maiores = []
    soma = 0
    while True:
        pessoas['nome'] = str(input('Nome: '))
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()
        pessoas['idade'] = int(input('Idade: '))
        soma += pessoas['idade']
        conjunto.append(pessoas.copy())
        if pessoas['sexo'] == 'F':
            mulheres.append(pessoas.copy())
        escolha = str(input('Quer continuar? [S/N] ')).upper()
        if escolha == 'N':
            break
    media = soma/len(conjunto)
    for c in range(len(conjunto)):
        if conjunto[c]['idade'] > media:
            maiores.append(conjunto[c])
    print(f'Foram cadastradas {len(conjunto)} pessoas.')
    print(f'A média de idade é: {media:.2f}')
    print(f'A lista de mulheres é {mulheres}.')
    print(f'A lista com idade maior que a média é: {maiores}')
    
    jogador = {}
    Jogadores = []
    while True:
        jogador['nome'] = str(input('Nome: '))
        partidas = int(input('Quantas partidas ele jogou: '))
        gols = []
        total = 0
        for p in range(partidas):
            gols.append(int(input(f'Quantos gols na partida {p+1}: ')))
            total += gols[p]
        jogador['gols'] = gols[:]
        jogador['total'] = total
        Jogadores.append(jogador.copy())
        escolha = str(input('Quer continuar? [S/N] ')).upper()
        if escolha == 'N':
            break
    for c in Jogadores:
        for k, v in c.items():
            print(f'No campo {k} tem o valor {v}')
        print(f'O jogador {c["nome"]} jogou {len(c["gols"])} partidas')
        for i in range(len(c['gols'])):
            print(f'Na partida {i+1}, fez {c["gols"][i]} gols')
        print(f'Foi um total de {c["total"]} gols')
    while True:
        x = str(input('Mostrar dados de qual jogador? ')).upper()
        for j in Jogadores:
            if x == j['nome'].upper():
                print(f'Levantamento do jogador {j["nome"]}.')
                for c in range(len(j['gols'])):
                    print(f'No jogo {c+1} ele fez {j["gols"][c]} gols.')
        escolha = str(input('Quer mostrar dados de mais algum jogador? [S/N] ')).upper()
        if escolha == 'N':
            break
    
    pessoas = {}
    for c in range(1):
        pessoas['nome'] = str(input('Nome: '))
        pessoas['idade'] = int(datetime.now().year-int(input('Qual o ano de nascimento: ')))
        pessoas['CTPS'] = int(input('nº da carteira de trabalho: '))
        if pessoas['CTPS'] != 0:
            pessoas['ano de contratação'] = int(input('Ano de contratação: '))
            pessoas['salario'] = float(input('Salário: '))
            x = 60 - (pessoas['idade'] + (datetime.now().year-pessoas['ano de contratação']))
            pessoas['idade de aposentar'] = pessoas['idade'] + x
    for k, v in pessoas.items():
        print(f'{k}: {v}')
    
    jogadores = {'Jogador_1':randint(1,6), 'Jogador_2':randint(1,6), 'Jogador_3':randint(1,6), 'Jogador_4':randint(1,6)}
    print('Valores sorteados')
    for k, v in jogadores.items():
        print(f'O {k} tirou {v}.')
        sleep(1)
    ranking = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
    print('Ranking dos Jogadores')
    c = 1
    for k, v in ranking.items():
            print(f'{c}º lugar: {k} com {v}')
            c +=1

    alunos = dict()
    sala = []
    for c in range(2):
        alunos['nome'] = str(input('Aluno: '))
        alunos['media'] = float(input(f'Qual a média de {alunos["nome"]}: '))
        if alunos['media'] >= 7:
            alunos['situaçao'] = 'Aprovado'
        else:
            alunos['situaçao'] = 'Reprovado'
        sala.append(alunos.copy())
    for a in sala:
        for k, v in a.items():
            print(f'{k} é igual a {v}.')
