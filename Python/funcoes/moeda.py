from funcoes import variadas
def diminuir(a, b, formato=False):
    porc = b/100
    r = a - (a*porc)
    r = round(r, 2)
    if formato == True:
        return moeda(r)
    return r

def aumentar(a, b, formato=False):
    porc = b/100
    r = a + (a*porc)
    r = round(r, 2)
    if formato == True:
        return moeda(r)
    return r

def dobro(a,  formato=False):
    if formato == True:
        return moeda(a*2)
    return a*2

def metade(a,  formato=False):
    if formato == True:
        return moeda(a/2)
    return a/2

def moeda(a):
    return "R${:.2f}".format(float(a))

def resumo(a, b, c):
    variadas.escreva('RESUMO DO VALOR')
    print(f'Preço analisado {moeda(a)}')
    print(f'Dobro do preço {dobro(a, True)}')
    print(f'Metade do preço {metade(a, True)}')
    print(f'{b}% de aumento {aumentar(a, b, True)}')
    print(f'{c}% de redução {diminuir(a, c, True)}')
    
