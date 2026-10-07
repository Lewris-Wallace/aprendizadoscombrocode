valor1 = 11

temsol = True

if valor1 > 10 and valor1 < 20:
    print("O valor está entre 10 a 20")
elif valor1 <= 5 or valor1 >= 20:
    print("O valor é menor ou igual a 5 ou maior ou igual a 20")

if not temsol:
    print("Está ensolarado")
else:
    print("Não está ensolarado")

print("O valor da variável 'valor1' é positiva?\n" \
"|||\n" \
"vvv") 
print("Sim" if valor1 > 0 else "Não")
print("=" * 45)
print("O valor da variável 'valor1' é ímpar ou par?")
print("Par" if valor1 % 2 == 0 else "Ímpar")
print("=" * 45)

numero1 = 15
numero2 = 5


valor_maximo = numero1 if numero1 > numero2 else numero2
valor_minimo = numero1 if numero1 < numero2 else numero2
# Lembrando que quando se faz if e else em uma única linha, o primeiro argumento antes do if, é o resultado caso a condição seja verdadeira, 
# e o segundo argumento depois do else, é o resultado caso a condição seja falsa.
print(f"O valor máximo entre {numero1} e {numero2} é {valor_maximo}")       
print(f"O valor mínimo entre {numero1} e {numero2} é {valor_minimo}")