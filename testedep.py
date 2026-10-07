cavalo = "bigorna"
numero = 20
numero2 = -1
numero = float(numero)
numeromod = bool(numero2)

x = 2
y = 2.0
x = x / y

print(numero)
print('--------------------')
print(type(numero), "tipo de dado mostrado na variável 'numero'")
print('--------------------')
print(numeromod, "| tipo de dado mostrado na variável 'numeromod' utilizando conceito boolean")
print('--------------------')
print(cavalo * 2)
print('--------------------')
print(type(cavalo))
print('--------------------')
print(10 % 4)
print('--------------------')
print(x, "| Quando você mistura a operação de um número inteiro com um número decimal, o resultado será um número decimal.")

nome = input("Qual é o seu nome? ")
altura = input("Qual é a sua altura? ")
peso = input("Qual é o seu peso? ")
imc =  float(peso) / (float(altura) ** 2)
print(f'Olá {nome}, sua altura é {altura} metros.')
print(f'Seu IMC é: {round(imc, 4)}')
print(f'Seu IMC é: {imc:.2f}')  # Formatação para duas casas decimais
print('--------------------')
print(type(f'{imc:.2f}')) # Utilizando o f-string para formatar o IMC, faz com que o tipo de dado seja uma string
print(type(round(imc, 4))) # Utilizando a função round() para arredondar o IMC, faz com que o tipo de dado seja um float

#estudante = input("Você é estudante? (sim/não): ")
#if estudante.lower() == "sim" or estudante.lower() == "s":
 #   print("Você é um estudante!")
#else:
 #   print("Você não é um estudante.")
