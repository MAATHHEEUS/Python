class fibonacci:
    print('SEQUÊNCIA DE FIBONACCI!!!')
    n = int(input('Quantos termos deseja mostrar? '))-2
    primeiro = 0
    segundo = 1
    print(f't0: {primeiro}')
    print(f't1: {segundo}')
    c = 2
    while True:
        if n > 0:
            proximo = segundo+primeiro
            primeiro = segundo
            segundo = proximo
            print(f't{c}: {proximo}')
            n -= 1
            c += 1
        else:
            escolha = str(input('quer mostrar mais termos? [S/N] ')).upper()
            if escolha == 'S':
                n = int(input('quantos? '))
            else:
                break
        
    
