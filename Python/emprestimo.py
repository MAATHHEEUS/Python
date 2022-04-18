class emprestimo:
    valor = float(input('qual o valor da casa? '))
    salario = float(input('qual seu salário? '))
    anos = int(input('em quantos anos deseja pagar? '))
    mensalidade = valor/(anos*12)
    if mensalidade > salario*0.3:
        print('o valor da mensalidade ficou R${:.2f}'.format(mensalidade))
        print('seu empréstimo foi negado! sinto muito')
    else:
        print('o valor da mensalidade ficou R${:.2f}'.format(mensalidade))
        print('PARABÉNS! seu empréstimo foi aceito')
