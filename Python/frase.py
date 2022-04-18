class frase:
    frase = 'PALMEIRAS MAIOR CAMPEÃO BRASILEIRO'
    nome = str(input('digite seu nome completo: '))
    splitado = nome.split()#separa o nome
    print(nome.upper())
    print(nome.lower())
    print('o nome tem {} letras'.format(len(nome)-nome.count(' ')))#conta quantas letras tem o nome
    print('tem silva no nome: {}'.format('SILVA' in nome.upper()))#verifica se tem silva no nome
    print('o primeiro nome é: {}'.format(splitado[0]))
    print('o último nome é: {}'.format(splitado[len(splitado)-1]))
    numero = str(input('digite um número entre 0 e 9999: '))
    numero = numero.zfill(4)
    print('unidade: {}.'.format(numero[len(numero)-1]))
    print("dezena: {}.".format(numero[len(numero)-2]))
    print('centena: {}.'.format(numero[len(numero)-3]))
    print('milhar: {}.'.format(numero[len(numero)-4]))
    cidade = str(input('digite o nome da cidade: '))
    print('começa com santo? {}'.format('SANTO' in cidade[0:6].upper()))
    f = str(input('digite uma frase qualquer: '))
    print("existem {} letras A's na frase".format(f.count('A')))
    print('a primeira letra A esta em {}'.format(f.find('A')))
    print('a última letra A esta em {}'.format(f.rfind('A')))
    
