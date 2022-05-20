from funcoes import variadas
class Jogo:
    palavrasIngles = ['Analytics', 'Business', 'Costumer', 'Intelligence']
    palavrasPortugues = ['Análise', 'Negócio', 'Consumidor', 'Inteligência']
    variadas.escreva("BEM VINDO! Vamos jogar")
    i = 0
    while i < len(palavrasPortugues):
        palavra = input(f'Digite a tradução da palavra: {palavrasIngles[i]} ').upper()
        if palavra != palavrasPortugues[i].upper():
            variadas.escreva(f'QUE PENA, VOCÊ ERROU!')
            break
        else:
            i+=1
    if i == len(palavrasPortugues):
        variadas.escreva('PARABÉÉÉNSSS!!!! VOCÊ VENCEU!!!')
    variadas.escreva("VOLTE SEMPRE PARA JOGAR!")    