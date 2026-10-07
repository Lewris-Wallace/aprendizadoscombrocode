nome = input("Digite o seu nome ou digite 'q' para sair: ")

while not nome.lower() == 'q':
    print(f"Olá, {nome}!")
    nome = input("Digite o seu nome ou digite 'q' para sair: ")

print("Programa encerrado. Até logo!")