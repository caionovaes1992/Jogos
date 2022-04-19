import random

def jogar(): # definindo a função para chamar o jogo

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # condição: enquanto NÃO enforcou E NÃO acertou.
    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print('Ops, você errou! Faltam {} tentativas.'.format(7 - erros))

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('Fim do jogo!')
    input('Pressione <enter> para finalizar o jogo')


def imprime_mensagem_abertura():
    print('*' * 28)
    print('Bem vindo ao jogo de forca!')
    print('*' * 28)

def carrega_palavra_secreta():
    # transformar a palavra do jogo em uma palavra aleatória e não mais estática
    arquivo = open('palavras.txt', 'r')
    palavras = []
    # laço para ler linha do arquivo "palavras" onde estão nossas palavras a serem escolhidas aleatoriamente pelo jogo
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    # randomizando a palavra secreta
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]  # ao invés de criar outro for fora, criamos dentro da lista.

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()  # retira os espaço desnecessários do início e fim da palavra e também coloca o chute em letras maiusculas

    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    # laço para saber se a letra escolhida está dentro da palavra secreta.
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():  # coloca todas as letras em maiúsculas (UPPER)
            letras_acertadas[index] = letra  # vai guardar as letras acertadas na posição certa dentro da palavra.
        index += 1  # operador de incremento para diminuir o código (equivale a index + 1)

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == '__main__':
    jogar()
