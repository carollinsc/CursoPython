
"""
Condições: IF, ELIF e ELSE
"""

if False:
    print(f'Esse é verdadeiro.')
elif False:
    print(f'O if foi falso e este é verdadeiro.')
else:
    print('Nenhum dos dois foi verdadeiro')
"""
Condições IF, ELIF e ELSE com operadores relacionais
"""

nome = input('Qual o seu nome? ')
idade = input("Qual a sua idade? ")
min_idade = 20
max_idade = 30

if min_idade <= int(idade) <= max_idade:
    print(f'{nome} pode pegar um empréstimo.')
else:
    print(f'{nome} está fora do intervalo aceito, portanto não pode pegar um empréstimo.')

"""
Operadores lógicos
and, or, not
in, e not in
"""

# and - só será verdadeiro se os dois ao mesmo tempo forem verdadeiros
# or - será verdadeiro se qualquer uma das comparações forem verdadeiras
# not - inverte a expressão: if b > a --> if not b > a
# in - está contido:
if 'u' in nome:
    print(f'Seu nome possui a letra u.')
else:
    print(f'Seu nome não possui a letra u.')
# not in - não está contido:
if 'u' not in nome:
    print(f'Seu nome não possui a letra u.')
else:
    print(f'Seu nome possui a letra u.')
