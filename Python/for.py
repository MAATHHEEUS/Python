from time import sleep
class foor:
    n = int(input('qual o número fatorial? '))
    fatorial = 1
    for c in range(1, n):
        fatorial *= (c+1)
    print(fatorial)
    
    for c in range(10, -1, -1):
        sleep(0.1)
        print(c)
    print('KBOOOM!!')

    n = 0
    for c in range(0, 501, 3):
        if c%2 == 0:
            n += c
    print('a soma de todos os números ÍMPARES múltiplos de 3 é: {}'.format(n))

    n = int(input('qual número deseja saber a tabuada? '))
    for c in range(11):
        print('{}x{}={}'.format(n, c, n*c))

    pa = int(input('qual a pa? '))
    r = int(input('qual a razão dessa pa? '))
    for c in range(0, 10):
        print(pa+c*r)

    n = int(input('qual é o número? '))# descobre sé um numero primo
    p = True
    for c in range(2, n):
        if n%c == 0:
            p = False
    print('é primo'if p == True else'não é primo')

    frase = str(input('qual é a frase? ')).strip().upper().split()
    #palavras = frase.split()
    junto = ''.join(frase)
    inverso = ''
    p = True
    for c in range(len(junto)-1, -1, -1):
        inverso += junto[c]
    for c in range(len(junto)-1):
        if inverso[c] != junto[c]:
            p = False
    print('é um palíndromo'if p == True else 'não é um palíndromo')
    
    nome = 'k'
    idade = 0
    sexo = 'f'
    soma = 0
    maiornome = 'o'
    conta = 0
    idademaior = 0
    for c in range(4):
        nome = str(input('qual o nome? '))
        idade = int(input('qual a idade? '))
        soma += idade
        sexo = str(input('qual o sexo F ou M? '))
        if sexo == 'F' and idade < 20:
            conta += 1
        elif sexo == 'M' and idade > idademaior:
            idademaior = idade
            maiornome = nome
    print('a média de idade é {.:2f}'.format(soma/4))
    print('o homem mais velho é {}'.format(maiornome))
    print('tem {} mulher(es) menor(es) de 20 anos'.format(conta))
        
