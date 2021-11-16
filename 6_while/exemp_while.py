"""
Utilizando 6_while para fazer uma espécie de calculadora

"""""

while True:
    print()
    num1 = input('Digite um número inteiro: ')
    num2 = input('Digite outro número inteiro: ')
    operador = input('Digite um operador (+, -, / ou *): ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == "s":
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')

    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    elif operador == "*":
        print(num1 * num2)
