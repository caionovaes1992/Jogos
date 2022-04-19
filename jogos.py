import adivinhacao
import forca

print('*' * 22)
print('Escolha o seu jogo...')
print('*' * 22)

# usuário escolhe qual jogo ele gostaria de jogar
print('[ 1 ] Forca  [ 2 ] Adivinhação')
jogo = int(input('Qual jogo você gostaria de jogar? '))

# inicialização do jogo de acordo com escolha do usuário
if jogo == 1:
    print('Jogando jogo da forca')
    forca.jogar() # chamando o jogo escolhido
elif jogo == 2:
    print('Jogando jogo da adivinhação')
    adivinhacao.jogar() # chamando o jogo escolhido
