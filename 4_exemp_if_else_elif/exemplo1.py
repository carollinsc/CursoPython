"""
"""

"""
Faça um programa que peça ao usuário para digitar um numero inteiro, informe se esse número é par ou impar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero = input('Por favor, digite um número inteiro: ')

if numero.isnumeric():
    numero = int(numero)

    if (numero % 2) == 0:
        print('O número digitado é par.')
    else:
        print('O número digitado é ímpar.')
else:
    print('O número digitado não é inteiro.')
