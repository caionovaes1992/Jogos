import random

def jogar(): # definindo a função para chamar o jogo

    print('*' * 35)
    print('Bem vindo ao jogo de adivinhação!')
    print('*' * 35)

    # declarando nossas variáveis
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    # escolhendo o nível do jogo a ser jogado
    print('Qual o nível de dificuldade?')
    print('[ 1 ] Fácil [ 2 ] Médio [ 3 ] Difícil')
    nivel = int(input('Escolha um nível: '))

    # definindo o número de tentativas do usuário de acordo com o nível escolhido
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # laço de tentativas do usuário
    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    # "chute" do usuário e verificando se ele acertou o número secreto e, se errou, informando se o chute é maior ou menor.
        chute = int(input('Digite um número entre 1 e 100: '))
        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = numero_secreto < chute
        print('Você digitou {}.'.format(chute))

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        if acertou:
            print('Parabéns! Você acertou e fez {} pontos!'.format(pontos))
            break

    # calculando, no caso de erros, quanto de ponto o usuário perdeu.
        else:
            pontos_perdidos = abs(numero_secreto - chute) # o abs transforma o número em um número absoluto
            pontos = pontos - pontos_perdidos
            if maior:
                print('Você errou! O número secreto é MAIOR do que seu chute.')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}. Você fez {} pontos.'.format(numero_secreto, pontos))
            elif menor:
                print('Você errou! O número secreto é MENOR do que seu chute.')
                if rodada == total_de_tentativas:
                    print('O número secreto era {}. Você fez {} pontos.'.format(numero_secreto, pontos))

    print('Fim do jogo!')
    input('Pressione <enter> para finalizar o jogo')

if __name__ == '__main__':
    jogar()
