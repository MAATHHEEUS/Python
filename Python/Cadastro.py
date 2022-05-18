from funcoes import variadas, dado
class cadastro:
    while True:
        dic = dict()
        pessoas = list()
        variadas.escreva('MENU PRINCIPAL')
        print('1 - cadastrar novas pessoas')
        print('2 - mostrar pessoas cadastradas')
        print('3 - sair')
        opcao = dado.leiaInt('Sua opção: ')
        if opcao == 1:
            variadas.escreva('CADASTRO DE PESSOAS')
            while True:
                while True:
                    dic['nome'] = str(input('Qual o nome da pessoa? '))
                    if str.isalpha(dic['nome']) == True:
                        break
                while True:
                    dic['idade'] = str(input('Qual a idade da pessoa? '))
                    if str.isnumeric(dic['idade']) == True:
                        break
                while True:
                    dic['sexo'] = str(input('Qual o sexo da pessoa? [F/M] ')).upper()
                    if dic['sexo'] == 'F' or dic['sexo'] == 'M':
                        break
                pessoas.append(dic.copy())
                while True:
                    escolha = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper()
                    if escolha == 'S' or escolha == 'N':
                        break
                if escolha == 'N':
                    break
            arquivo = open('PESSOAS.txt','a')
            for p in pessoas:
                arquivo.write(str(p)+'\n')
            arquivo.close()    
        elif opcao == 2:
            variadas.escreva('PESSOAS CADASTRADAS NO ARQUIVO')
            arquivo = open('PESSOAS.txt','r')
            for linha in arquivo:
                print(linha.rstrip())
            arquivo.close()
        elif opcao == 3:
            print('VOLTE SEMPRE!!!')
            break
        else:
            print('\033[1;31m VOCÊ DIGITOU UM VALOR FORA DAS OPÇÕES\033[1;0m')
                                      

