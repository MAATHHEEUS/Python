class While:

        while True:
            n = int(input('qual número quer saber a tabuada? '))
            if n < 0:
                break
            for c in range(1, 11):
                print(f'{n}x{c}={c*n}')
    
        n = 'x'
        menor = -1
        maior = media = soma = c = 0
        while n != 'N':
            c += 1
            n1 = int(input('digite um valor '))
            soma += n1
            media = soma/c
            if n1 > maior:
                maior = n1
            if n1 < menor or menor == -1:
                menor = n1
            n = str(input('quer digitar mais valores? [S/N] ')).upper()
        print(f'a média é {media:.2f}')
        print('o maior valor é {} e o menor {}'.format(maior, menor))
        
        r = int(input('qual a razão da pa? '))
        pa = int(input('qual o primeiro termo? '))
        c = 1
        n = 10
        while c < n+1:
            print(pa*c)
            c += 1
            if c == n+1:
                n += int(input('quer mostrar mais quantos termos? '))
        
        n = 'x'
        while 'M' != n != 'F':
            n = str(input('digite o sexo da pessoa [M/F]: ')).upper()
        print('a pessoa é {}'.format(n))

        import random
        n = random.randint(0, 1)
        tentativas = 0
        palpite = -1
        while n != palpite:
            tentativas += 1
            palpite = int(input('qual número o computador escolheu'))
        print('você precisou de {} palpites para acertar'.format(tentativas))

        n = -1
        while n != 5:
            n1 = int(input('digite um valor '))
            n2 = int(input('digite outro valor '))
            n = int(input("""oque deseja fazer com eles:
                    [1]somar
                    [2]multiplicar
                    [3]maior
                    [4]novos valores
                    [5]sair do programa
                    """))
            if n ==1 :
                print('a soma dos valores é {}'.format(n1+n2))
            if n == 2 :
                print('a multiplicação dos valores é {}'.format(n1*n2))
            if n == 3 :
                if n1 > n2:
                    print('{} é o maior valor'.format(n1))
                else:
                    print ('o maior valor é: {}'.format(n2))

        n = int(input('qual o número que deseja saber o fatorial? '))
        c = 1
        fatorial = 1
        while c < n :
            fatorial *= (c+1)
            c += 1
        print(fatorial)
            
