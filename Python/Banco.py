class banco:
    print('='*30)
    print('BANCO X')
    print('='*30)
    valor = int(input('Qual valor deseja sacar? R$'))
    u = valor % 10
    d = valor % 100
    valor = valor - u - d
    cm = valor/50
    if u != 0:
        print(f'total de {u} cédulas de R$1')
    if d != 0:
        if int(d/50) != 0:
            d = d%50
            cm += 1
        if int(d/20) != 0:
            print(f'total de {int(d/20)} cédulas de R$20')
            d = d%20
        if int(d/10) != 0:
            print(f'total de {int(d/10)} cédulas de R$10')
    if cm != 0:
        print(f'total de {cm:.0f} cédulas de R$50')
        
