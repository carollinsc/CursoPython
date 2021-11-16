""""
Entrada de dados
"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nascimento = 2021 - int(idade)

print()
print(f'O usuário se chama {nome} e tem {idade} anos de idade. '
      f'Seu ano de nascimento foi {ano_nascimento}.')

"""
Calculadora
"""
numero1 = int(input("Por favor, digite um número: "))
numero2 = int(input("Por favor, digite outro número: "))
soma = numero1 + numero2

print(f"A soma dos números digitados é: {soma}")
