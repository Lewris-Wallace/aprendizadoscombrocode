triplos = []

for i in range(1, 11):
 triplos.append(i * 3)

print(triplos)
print('-' * 30)

duplos = [i * 2 for i in range(1, 11)]
print(duplos)
print('-' * 30)

palavras = ["Judeu", "Cavalo", "Lucas", "Deuzebu"]
palavras1 = [palavra.upper() for palavra in palavras]
indexacao_1 = [index[1] for index in palavras]

print(palavras1)
print(indexacao_1)
print('-' * 30)

numeros_positivos = [numero for numero in [1, -3, 2, 6, -5, 3] if numero >= 0]
print(numeros_positivos)
print('-' * 30)

notas = [0, 3, 8, 4, 6, 4, 1, 7, 9, 10]
notas = [print(f'Você passou! Sua nota foi {nota}!') for nota in sorted(notas) if nota >= 6]