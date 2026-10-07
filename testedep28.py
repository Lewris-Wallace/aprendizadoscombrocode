
nomes = ["Clara", "João", "Matheus"]


print("Olá! Estaremos apresentando nossa classe Delta!")
print("-" * 30)
while True:
    print("Nós temos estes alunos:")
    for nome in nomes:
        print(nome)
    print("-" * 30)

    nome1 = input("Você gostaria de adicionar um novo aluno? Se sim, digite algo ou digite 'q' para sair: ")

    if nome1 == 'q' or nome1 == 'Q':
        print("A sua classe está oficialmente formada!\n" \
        "Esses são os alunos:")\
        
        for nome in nomes:
            print(nome)
        print("Obrigado por testar o programa! Até mais outra vez!")
        break

    if nome1 not in nomes:
        print("Um novo aluno foi adicionado!")
        nomes.append(nome1)
 
    elif nome1 in nomes:
        print(f"O aluno {nome1} existe, por obséquio, coloque outro nome para prosseguir:")
        continue