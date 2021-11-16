''
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos, escreva "Seu nome é curto";
Se tiver entre 5 e 6 letras escreva "Seu nome é normal"; maior que 6 letras escreva "Seu nome é muito grande".
"""

nome = input('Por favor, digite seu primeiro nome: ')
qtdcaracteres = len(nome)

if qtdcaracteres <= 4:
    print('Seu nome é curto.')
elif qtdcaracteres <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')