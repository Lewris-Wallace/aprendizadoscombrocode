comidas = {"pizza": 3.25,
           "cachorro-Quente": 2.35,
           "coxinha": 3.00,
           "pastel": 2.66,
           "doce de Goiaba": 3.13,
           "pudim": 5.12}

carrinho = []
total = 0
print('-' * 9, 'MENU', '-' * 9)
for comida, valor in comidas.items():
    print(f'{comida.capitalize():16}: {valor:.2f}R$')
print('-' * 24)
