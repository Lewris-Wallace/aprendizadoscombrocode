lista1 = ["loucura", "doideira", "oi"]
lista2 = ["parede", "macaco", "rato"]
lista3 = ["colher", "geladeira", "astuto"]

listamesclada = ["loucura", "doideira", "oi"], ["parede", "macaco", "rato"], ["colher", "geladeira", "astuto"]
listamesclada2 = [lista1, lista2, lista3]

print(listamesclada2)


for colecao in listamesclada:
    for colecao2 in colecao:
     print(colecao2, end = " ")
    print()