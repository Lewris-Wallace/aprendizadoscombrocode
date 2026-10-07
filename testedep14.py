comidas = []

while True:
    comida = input("Digite qualquer nomenclatura de comida, e digite 'q' para sair: ")
    
    if comida.lower() == "q":
        print("Fim do programa!")
        break

    comida = comidas.insert(1, comida)
    print(comidas)