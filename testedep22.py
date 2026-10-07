# Projeto de encriptação

import random
import string

caracteres = " " + string.ascii_letters + string.digits + string.punctuation
caracteres = list(caracteres)
chave = caracteres.copy()
random.shuffle(chave)


# print(f"Lista de caracteres: {caracteres}")
print('-' * 25)
# print(f"Lista de caracteres com a chave: {chave}")
print('-' * 25)
print(caracteres.index('f'))

texto_normal = input('Digite um texto para criptografia: ')
texto_criptografado = ""

for letra in texto_normal:
    index = caracteres.index(letra)
    texto_criptografado += chave[index]

print(f"Este é o texto inserido: {texto_normal}")
print(f"Este é o texto criptografado: {texto_criptografado}")