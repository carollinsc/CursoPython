"""
Trata-se de um jogo de adivinhação, tipo forca, onde o usuário irá digitar uma letra para tentar acertar a palavra
secreta.
"""
secreta = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ah não, você só pode digitar 1 letra.')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'Uhulll, a letra "{letra}" está na palavra secreta.')

    else:
        print(f'A letra "{letra}" não faz parte da palavra secreta.')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreta:
        print(f'Que legal, você ganhou! A palavra era: {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreta:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
        print()
