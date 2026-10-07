nome = 'Alessandro da Silva'

letras = "asfgs"
letrasenumeros = "asfgs123"
numero = "1234"

print(len(nome))

print(nome.rfind("a"))

primeiraletram = nome.capitalize()

print(primeiraletram)
# ---------
print(letras.isdigit())
print(letrasenumeros.isdigit())
print(numero.isdigit())
print("-" * 10)
# O conteúdo é apenas verdadeiro, se tiver apenas números.
# --------
print(nome.count("a"))
print("-" * 10)
# --------
print(letras.isalpha())
print(letrasenumeros.isalpha())
print(numero.isalpha())
print(nome.isalpha())
print("-" * 10)
# O conteúdo é apenas verdadeiro, se tiver apenas letras, e não pode houver nem espaços ou números juntos


for i in range(len(nome)):
    if nome[i] == "a":
        print(f"Letra 'a' encontrada na posição {i}")