import random
class tuplas:
    palavras = 'ARROZ', 'FEIJAO', 'COUVE', 'FAROFA'
    for palavra in palavras:
        print(f'\nNa palavra {palavra} temos as vogais: ', end = '')
        for letra in palavra:
            if letra.upper() in 'AEIOU':
                print(letra, end = ' ')
        
    listagem = 'Pão', 1, 'Café', 3.99
    print(f'\nLISTAGEM DE PREÇO')
    for i in range(0, len(listagem), 2):
        print(f'{listagem[i]} R${listagem[i+1]}')
                   
    a = int(input('digite o primeiro valor: '))
    b = int(input('digite o segundo valor: '))
    c = int(input('digite o terceiro valor: '))
    d = int(input('digite o quarto valor: '))
    valores = a, b, c, d
    print(f'o valor 9 aparece {valores.count(9)} vezes')
    if 3 in valores:
        print(f'a primeira ocorrencia de 3 é na posição {valores.index(3)+1}')
    else:
        print('o valor 3 não aparece em nenhuma posição')
    print('os números pares foram: ')
    for v in valores:
        if v%2 == 0:
            print(v)
    
    aleatorio = int(10*random.random()), int(10*random.random()), int(10*random.random()), int(10*random.random()), int(10*random.random())
    menor = maior = aleatorio[0]
    for c in aleatorio:
        if menor > c:
            menor = c
        if maior < c:
            maior = c
    print(f'os números sorteados são: {aleatorio}')
    print(f'o maior número da tupla é {maior} e o menor é {menor}')
    
    camp = 'PAL', 'FLA', 'CAM', 'COR', 'SAO', 'AME', 'FLU', 'BOT', 'SAN', 'AVA', 'BRA', 'INT', 'ATL', 'ATG', 'CEA', 'COR', 'CUI', 'FOR', 'GOI', 'JUV'
    print(f'os 5 primeiros são:')
    for c in range(5):
        print(camp[c])
    print(f'os rebaixados são:')
    for c in range(-1, -5, -1):
        print(camp[c])
    print(sorted(camp))
    print(f'o PALMEIRAS está em {camp.index("PAL")+1}º colocado')
    
    extenso = 'zero', 'um', 'dois', 'tres'
    while True:
        n = int(input('digite um número de 0 a 3 '))
        if n in range(0,4):
            break
    print(extenso[n])
