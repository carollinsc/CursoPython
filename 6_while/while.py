x = 0

while x < 5:
    y = 0
    while y < 5:
        print(f'{x},{y}.')
        y = y + 1  # também pode ser escrito como y += 1
    x = x + 1

print('Acabou.')
