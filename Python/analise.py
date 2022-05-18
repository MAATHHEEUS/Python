class analise:
    n = input("digite algo: ")
    print('É do tipo: ', type(n))
    print('É numérico: {}'.format(n.isnumeric()), end="\n")
    print('É alfa númerico {}'.format(n.isalnum()))
    print('Está em maiúsculo: {}'.format(n.isupper()))
    print('É alfabético {}'.format(n.isalpha()))
    print('É um espaço {}'.format(n.isspace()))
