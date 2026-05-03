precio = input('Cuál es el precio? ')
precio = float(precio)
if precio>100000:
    print(f'El precio final es {precio*0.8}')
elif precio>50000:
    print(f'El precio final es {precio*0.9}')
else:
    print(f'El precio final es {precio}')
