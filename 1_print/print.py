nome = "Caroline"
idade = 24
altura = 1.58
e_maior = idade > 18
peso = 68
imc = peso / (altura ** 2)

print(nome, "tem", idade, "anos de idade, e o seu imc é:", imc)
print(f'{nome} tem {idade} anos de idade, e o seu imc é: {imc:0.2f}')
