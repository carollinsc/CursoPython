""""""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
0-11 Bom dia!
12-17 Boa tarde!
18-23 Boa noite!
"""

hora = input('Por favor, digite a hora (0-23): ')
if hora.isnumeric():
    hora = int(hora)

    if 0 <= hora <= 11:
        print('Bom dia!')
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    elif 18 <= hora <= 23:
        print('Boa noite!')
    elif hora < 0 or hora > 23:
        print('A hora deve estar entre 0 e 23.')
else:
    print('Esta hora não é válida.')
