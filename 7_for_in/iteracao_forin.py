for n in range(0, 100, 1):
    print(n)  # vai mostrar cada número, começando em 0, pulando de 1 em 1, até 99 (o 100 não entra)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()  # .upper() vai tornar a letra maiúscula
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)