nome = 'Luiz'
idade = 32
altura = 1.8
peso = 80.5
imc = peso / altura ** 2
anoatual = 2021
nascimento = anoatual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.')
print(f'O IMC de {nome} é {imc :0.2f}.')
print(f'{nome} nasceu em {nascimento}.')
