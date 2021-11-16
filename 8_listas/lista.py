"""
Listas são conjuntos de variáveis, que podem receber valores de vários tipos diferentes
append, insert, pop, del, clear, extend, +
máx, mín
range
"""""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2  # neste caso, o + vai concatenar as duas listas, entregando [1, 2, 3, 4, 5, 6]
l1.extend(l2)  # neste caso, l1 vai receber o valor de l1 concatenado com l2
l1.insert(0, '4, 5, 6')  # estamos inserindo a string '4, 5, 6' no índice 0, ou seja, iniciando a lista l1.
                         # não é uma substituição, é uma adição.
l1.pop()  # exclui a última variável da lista
l1.del(2)

