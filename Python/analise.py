class analise:
    _n = ''
    def get_n(self):
        return self._n
    
    def set_n(self, dado):
        if(dado == ''):
            print('Digite algo para ser analisado!')
        else:
            self._n = dado

    def __init__(self, dado) -> None:
        self._n = dado

    if(_n == ''):    
        n = input("digite algo: ")

    print('É do tipo: ', type(n))
    print('É numérico: {}'.format(n.isnumeric()), end="\n")
    print('É alfa númerico {}'.format(n.isalnum()))
    print('Está em maiúsculo: {}'.format(n.isupper()))
    print('É alfabético {}'.format(n.isalpha()))
    print('É um espaço {}'.format(n.isspace()))