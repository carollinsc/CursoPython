"""
For / Else em Python
"""

variavel = ['Luiz Otavio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):  # .lower() vai transformar de maiús p minús, ..startswith vai checar se começa
        print(f'{valor}')
        break
else:
        print('Não existe uma palavra que começa com J.')