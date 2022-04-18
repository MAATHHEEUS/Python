class lista:
    alunos = list()
    dado = list()
    while True:
        dado.append(str(input('Nome do aluno: ')))
        dado.append(float(input('Qual a 1ª nota: ')))
        dado.append(float(input('Qual a 2ª nota: ')))
        alunos.append(dado[:])
        dado.clear()
        escolha = str(input('Quer continuar? S/N ')).upper()
        if escolha == 'N':
            break
    for a in alunos:
        print(f'O aluno {a[0]} teve média igual a: {(a[1]+a[2])/2:.2f}')
    while True:
        escolha = str(input('Deseja mostrar notas de qual aluno? '))
        for a in alunos:
            if escolha == a[0]:
                print(f'As notas de {escolha} são: {a[1]} e {a[2]}')
            else:
                print(f'Aluno {escolha} não está na lista!')
        e = str(input('Quer continuar? S/N ')).upper()
        if e == 'N':
            break
    
    matriz = [[], [], []]
    somaPares = somaTerceiraColuna = maiorSegunda = 0
    for i in range(3):
        for j in range(3):
            matriz[i].append(int(input(f'Digite o valor para [{i}][{j}]: ')))
            if matriz[i][j]%2 == 0:
                somaPares += matriz[i][j]
            if j == 2:
                somaTerceiraColuna += matriz[i][j]
            if i == 1 and matriz[i][j] > maiorSegunda:
                maiorSegunda = matriz[i][j]
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(f'A soma do pares é: {somaPares}')
    print(f'A soma do valores da 3º coluna é: {somaTerceiraColuna}')
    print(f'O maior Valor da 2º linha é: {maiorSegunda}')

    pessoas = list()
    dado = list()
    maior = menor = 0
    while True:
        dado.append(str(input('Nome: ')))
        dado.append(float(input('Peso: ')))
        if dado[1] > maior:
            maior = dado[1]
        if menor == 0 or menor > dado[1]:
            menor = dado[1]
        pessoas.append(dado[:])
        dado.clear()
        escolha = str(input('Quer continuar? S/N ')).upper()
        if escolha == 'N':
            break
    print(f'Foram cadastradas {len(pessoas)} pessoas')
    print('As pessoas mais pesadas são: ', end = '')
    for p in pessoas:
        if p[1] == maior:
            print(p)
    print('As pessoas mais leves são: ', end = '')
    for p in pessoas:
        if p[1] == menor:
            print(p)
            
    exp = [str(input('Digite uma expressão com parênteses: '))]
    if exp[0].count('(') == exp[0].count(')'):
        print('Sua expressão é válida')
    else:
        print('Sua expressão não é válida')
        
    numeros = [[], []]
    for c in range(4):
        n = int(input('digite um valor: '))
        if n%2 == 1:
            if numeros[0] == '':
                numeros[0].append(n)
            else:
                pos = 0
                for i in range(len(numeros[0])):
                    if n > numeros[0][i]:
                        pos += 1
                numeros[0].insert(pos, n)
        else:
            if numeros[1] == '':
                numeros[1].append(n)
            else:
                pos = 0
                for i in range(len(numeros[1])):
                    if n > numeros[1][i]:
                        pos += 1
                numeros[1].insert(pos, n)
    print(f'A lista de números é {numeros}')
    print(f'Apenas números pares: {numeros[1]}')
    print(f'Ímpares: {numeros[0]}')
    
    lista = []
    maior = menor = 0
    while True:
        n = int(input('digite um valor: '))
        if n in lista:
            print('este valor ja existe na lista')
        else:
            lista.append(n)
            print('valor adicionado com sucesso')
        escolha = str(input('deseja continuar? S/N ')).upper()
        if escolha == 'N':
            break
    for num in lista:
        if num > maior:
            maior = num
        if num < menor or menor == 0:
            menor = num
    print(f'O maior valor é {maior} e está na posição {lista.index(maior)}')
    print(f'O menor valor é {menor} e esta na posição {lista.index(menor)}')
    print(f'Foram inseridos {len(lista)} valores a lista')
    if 5 in lista:
        print(f'O valor 5 foi digitado e está na posição {lista.index(5)}')
    lista.sort()
    print(f'A lista em ordem cresceste é {lista}')
    lista.sort(reverse=True)
    print(f'A lista em ordem decrescente é {lista}')
