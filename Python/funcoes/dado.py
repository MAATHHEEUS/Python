def leiaDinheiro(msg):
    while True:
        try:
            p = input(msg).replace(',','.')
            if p.isalpha() or p.strip() == '':
                print('ERRO! DIGITE UM VALOR MONETÁRIO')
            else:
                return float(p)
        except ValueError:
            print('ERRO! DIGITE SOMENTE NÚMEROS COM VÍRGULA!')
        
    
def leiaInt(frase):
    """
    Verifica se um número é inteiro, caso não for da uma mensagem de erro e tenta ler novamente.
    """
    try:
        while True:
            n = str(input(frase))
            if n.isnumeric() == True:
                return int(n)
            else:
                print('ERRO, DIGITE UM VALOR INTEIRO!')
    except KeyboardInterrupt:
        print('O USUÁRIO DECIDIU NÃO DIGITAR O VALOR')
        return 0
