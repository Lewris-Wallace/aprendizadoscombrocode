linha = int(input('Coloque o número de linhas: '))
coluna = int(input("Coloque o número de colunas: "))
simbolo = input("Agora coloque algum símbolo para aparecer nas linhas e colunas respectivas: ")

for linhas in range(linha):
    for colunas in range(coluna):
     print(simbolo, end="")
    print()