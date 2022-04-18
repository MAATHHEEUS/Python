import random;
class condicional:
    x = random.randint(0,5)
    y = int(input('qual número o computador sorteou? '))
    if x == y:
        print('PARABÉNS você acertou')
    else:
        print('você errou. QUE PENA')

    vel = float(input('qual a velocidade do carro? '))
    if vel > 80:
        print('você ultrapassou o limite de velocidade!')
        print('o valor da multa ficou R${:.2f}'.format((vel-80)*7))

    n = int(input('digite um número inteiro '))
    print('é par'if n%2 == 0 else 'é ímpar')

    d = float(input('qual a distância da viajem em kg '))
    if d <= 200:
        print('o valor da viagem ficou R${}'.format(d*0.5))
    else:
        print('o valor da viagem ficou R${}'.format(d*0.45))

    ano = int(input('qual é o ano '))
    print('esse ano é bissexto' if ano%4 == 0 else 'o ano não é bissexto')

    n1 = float(input('qual o primeiro número '))
    maior = n1
    menor = n1
    n2 = float(input('qual o segundo número '))
    if n1 < n2:
        maior = n2
    else:
        menor = n2
    n3 = float(input('qual o terceiro '))
    if maior < n3:
        maior = n3
    if menor > n3:
        menor = n3
    print('o maior número é {} e o menor é {}'.format(maior, menor))

    s = float(input('qual o salário do funcionário '))
    if s > 1250:
        print('o aumento vai ser de R${:.2f}'.format(s*0.1))
    else:
        print('o aumento vai ser de R${:.2f}'.format(s*0.15))

    r1 = float(input('qual o comprimento da primeira reta: '))
    r2 = float(input('qual o comprimento da segunda reta: '))
    r3 = float(input('qual o comprimento da terceira: '))
    if r1 > abs(r2-r3) and r1 < (r2+r3):
        print('essas retas formam um triângulo')
        if r1 == r2 == r3:
            print('e esse triângulo é  equilatero')
        elif r1 == r2 or r1 == r3 or r2 == r3:
            print('e esse triângulo é isóceles')
        else:
            print('e esse triângulo é escaleno')
    elif abs(r1-r2) < r3 < r1+r2:
        print('essas retas formam um triângulo')
        if r1 == r2 == r3:
            print('e esse triângulo é  equilatero')
        elif r1 == r2 or r1 == r3 or r2 == r3:
            print('e esse triângulo é isóceles')
        else:
            print('e esse triângulo é escaleno')
    elif abs(r1-r3) < r2 < r1+r3:
        print('essas retas formam um triângulo')
        if r1 == r2 == r3:
            print('e esse triângulo é  equilatero')
        elif r1 == r2 or r1 == r3 or r2 == r3:
            print('e esse triângulo é isóceles')
        else:
            print('e esse triângulo é escaleno')
    else:
        print('essas retas não formam um triângulo')

    
    
