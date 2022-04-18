import random
from time import sleep
class MEGASENA:
    jogos = list()
    jogo = list()
    n = int(input('Quantos jogos deseja fazer? '))
    for c in range(n):
        jogo = random.sample(range(1, 60), 6)
        jogo.sort()
        print(f'{c+1}º jogo: {jogo}')
        sleep(0.5)
        jogos.append(jogo[:])
        jogo.clear()
    print(f'A lista completa com todos os jogos é: {jogos}')
        
