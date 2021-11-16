print('Olá, mundo!')  # Comentário
print('Luiz', 'Otávio', sep='-')
print('Maria', 'João', end='///', sep='-')
print('Carla')

print('075.220.345-34')
print('075', '220', '345', sep='.', end='-')
print('34')

print('Aspas simples')  # aspas simples/duplas indicam string, o programa consegue entender que é um texto
print("Essa é uma 'string' (str)")  # ou 'Essa é uma "string" (str).'
print(r"Essa é uma 'string'' (str).")  # r antes da string indica q nada deve ser executado dentro das ", q é tudo texto

""""
Tipos de dados
str - string - texto -> 'Assim' ou "Assim"
int - inteiro - é um número positivo ou neg ou 0 sem casas decimais -> 3 -9 0 23
float - real/ponto flutuante - número com decimais -> 0,45 -5,6 2,345
bool - booleano/lógico - true/false 
"""

print('Luiz', type('Luiz'))  # string
print(10, type(10))  # int
print(25.23, type(25.23))  # float
print(10 == 10, type(10 == 10))  # bool

# nome: string
print("Caroline", type("Caroline"))

# idade: int
print(24, type(24))

# Altura: float
print(1.58, type(1.58))

# É maior de idade: booleana
print(24 > 18, type(24 > 18))

""""
Operadores Aritméticos
+ - soma
- subtração
* - multiplicação
/ - divisão
// - divisão inteira
** - exponenciação
% - módulo
"""
print("Soma (+) ", 10 + 10)
print("Subtração (-) ", 10 - 10)
print("Multiplicação (*) ", 10 * 10)
print("Divisão (/) ", 10 / 10)

print("20" + "A")  # quando somamos 2 strings, concatena, ou seja, junta as duas
print(20 * "A")  # quando multiplicamos um número por uma string, repete a qtd de vezes

"""
Precedência de operadores
Parênteses ()
Exponenciação **
Multiplicação, divisão, divisão inteira e módulo  * / // %
Soma e subtração + -
Lista com todos os operadores em python https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

"""
Variáveis
Precisa: iniciar com letra, pode conter números, separar com _, letras minúsculas
"""

nome = "Caroline"
idade = 24
altura = 1.58
e_maior = idade > 18
peso = 68
imc = peso / (altura ** 2)

print("Meu nome é: ", nome)
print("Eu tenho ", idade, "anos")
print("Meço ", altura)
print("Sou maior de idade? R: ", e_maior)

print(nome, " tem ", idade, " anos de idade, e o seu imc é: ", imc)
