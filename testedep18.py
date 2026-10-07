comidas = {"pizza": 3.25,
           "cachorro-quente": 2.35,
           "coxinha": 3.00,
           "pastel": 2.66,
           "doce de goiaba": 3.13,
           "pudim": 5.12}


comidas2 = comidas.items()

carrinho = []
dinheiro = 20

print("Olá! Este é o cardápio:")
for comida, valor in comidas2:
    print(f'{comida} | {valor}R$')
print('---------------------------')
while True:
    pegando = input('Escolha alguma opção do cardápio, senão, aperte "q" para finalizar suas compras : ').lower()

    if pegando == "q":
        print(f"Nossa! Hoje foi um dia bem histórico, não é mesmo? Você pegou esses itens: {carrinho}, e seu saldo é de: {dinheiro}R$")
        print(f"Volte mais tarde para outras compras!")
        break

    if pegando not in comidas:
        print("Não existe esta opção no cardápio, escolha certo.")
        continue

    if comidas[pegando] > dinheiro: 
            print(f'Você não pode realizar a compra, seu dinheiro atual é de {dinheiro:.2f}R$')
            continue

    dinheiro -= comidas[pegando]
    carrinho.append(pegando)
     
    print(f'Uou, você pegou {pegando}')
    print(f'Agora, você tem o valor de {dinheiro:.2f} R$ para gastar')