import random

numeros = random.randint(1, 6)
numero2 = random.random() # Sai números aleatórios de 0 a 1.
jokenpo = ["pedra", "papel", "tesoura"]
embaralhar = ["oi", 2, 3, 6, 8, "cavalo", 3, "queisso", "b", "d", "f"] 
random.shuffle(embaralhar)

print(random.choice(jokenpo)) # vai escolher entre os três valores que está na variável "jokenpo"
print(embaralhar) # embaralha a sequência do valor da variável "embaralhar"
print(numeros)
print(numero2)