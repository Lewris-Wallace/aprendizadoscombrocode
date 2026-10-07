import math

numero1 = 5.3
numero2 = 3.7

print(math.e) # Valor de Euler, aproximadamente 2.718281828459045
# -

print(math.ceil(4.2)) # Arredonda para cima, retornando 5
print(math.floor(4.8)) # Arredonda para baixo, retornando 4
# Exemplos com variáveis:
print(math.ceil(numero1)) # Arredonda para cima, retornando 6
print(math.floor(numero2)) # Arredonda para baixo, retornando 3

# Exemplo dinâmico com uma circunferência:
input_raio = float(input("Digite o raio da circunferência: "))
circunferencia = 2 * math.pi * input_raio
print(f"A circunferência com raio {input_raio} é: {round(circunferencia, 6)}cm")