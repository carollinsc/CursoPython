"""
Split, join, enumerate em Python
split - divide as strings em variáveis de uma lista (só funciona com strings)
join - junta itens de uma lista (só funciona com strings)
enumerate - (funciona com iteraveis)
"""""
string = "Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')  # cada coisa que for dividida por um espaço, virará 1 variável da lista
lista_2 = string.split(',')  # cada coisa que for dividida por uma vírgula "     "    "      "   "

for valor in lista_1:
    print(f'A palavra {valor} aparece {lista_1.count(valor)}x na frase.')
