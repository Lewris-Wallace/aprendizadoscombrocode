index = ["ola", "hello", "hi", "greetings", "salutations"]

index2 = "loucuratal" 

print(index2[2:]) # Este index pega a partir do índice 2 até o final da string, ou seja, seria 2 até 10 ou 2:10 seguindo a lógica.
print("-" * 20)
print(index2[-3:]) # Este index pega três casas atrás do index 0, ou seja, as letras que vão sair, são "tal", 
#que são as três últimas letras da string.
print("-" * 20)
print(index2[:5]) # Este index pega do início da string até o índice 5 (exclusivo), é como fosse o seguinte, o valor que está vazio na esquerda, 
# seria zero.
print("-" * 20)
print(index2[::1]) # Este index pega a string inteira, pois o passo é 1, ou seja, ele vai percorrer a string inteira.
print("-" * 20)
print(index2[::2]) # Este index pega a string inteira, mas com passo 2, ou seja, ele vai percorrer a string inteira, mas vai pular uma letra.
print("-" * 20)
print(index2[::-1]) # Este index pega a string inteira, mas com passo -1, ele vai percorrer a string inteira, mas vai inverter a ordem das letras.
print("-" * 20)
print(index[2])

