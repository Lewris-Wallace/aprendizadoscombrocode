import time

for x in reversed(range(1, 11)):
    print(x)
    time.sleep(0.1)

print("Feliz Ano Novo!")

for y in range(1, 11):
    print(y)
    time.sleep(0.1)
print('-' * 20)

for z in range(1, 14, 3): # Imprime os números de 1 a 14, de 3 em 3, imprimindo os números 1, 4, 7, 10 e 13.
    print(z)
print('-' * 20)

teste_de_caracteres = "2356-2344-4-2-24-44"

for w in teste_de_caracteres:
    print(w) 
