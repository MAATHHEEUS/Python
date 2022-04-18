import random
class parOuImpar:

    print('VAMOS JOGAR PAR OU ÍMPAR')
    c = 0
    while True:
        n = int(input('digite um valor: '))
        pc = random.randint(0, 10)
        escolha = str(input('Par ou ímpar? [P/I] ')).upper()
        resultado = (n+pc)%2
        if resultado == 0:
            print(f'você jogou {n} e o pc jogou {pc}. Total {n+pc} deu par')
            if escolha == 'P':
                print(f'Você ganhou!')
                c += 1
            else: break
        if resultado != 0:
            print(f'você jogou {n} e o pc jogou {pc}. Total {n+pc} deu ímpar')
            if escolha == 'I':
                print(f'Você ganhou!')
                c += 1
            else:
                break
    print(f'Você PERDEU! Você venceu {c} vezes')
        
        
        
