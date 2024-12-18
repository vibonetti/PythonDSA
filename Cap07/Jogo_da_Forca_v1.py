# Projeto 1 - Desenvolvimento do jogo da forca em Python v1

#Import
import random
from os import system, name

#Função para limpar a tela em casa execução

def limpa_tela():
    #Windows
    if name == 'nt':
        _ = system('cls')
    #Mac ou Linux
    else:
        _ = system('clear')

#Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #lista de palavras
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolha randomicamente uma palavra
    palavra = random.choice(palavras)

    #list comprehension
    letras_descobertas = ['_' for letra in palavra]

    #numero de chances
    chances = 6

    #listra de letras erradas
    letras_erradas = []

    #Loop enquanto o numero de chances for maior do que zero
    while chances >0:

        #print
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        #condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break
    
    #Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

#bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você é o brabão do python")



