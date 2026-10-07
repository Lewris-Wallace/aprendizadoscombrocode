# Calculadora Python de Dois Números
import time 

while True:
 print("\n" + "=" * 45)
 
 operador = input("\nDigite algum operador para continuar:\n" \
 " '+' -> (adição) || '-' -> (subtração) || '*' -> (multiplicação) || '/'- > (divisão)\n"
 "Ou digite 'sair' para encerrar o programa: ")


 if operador in ["+", "-", "*", "/"]:
        break

 if operador.lower() == "sair":
        print("\nEncerrando o programa. Até logo!")
        exit()

 print("\nOperador inválido. Por favor, use +, -, * ou /.\n")
 time.sleep(1)  # Pausa de 1 segundos antes de solicitar novamente o operador


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado de {numero1} + {numero2} é: {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado de {numero1} - {numero2} é: {resultado}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado de {numero1} vezes {numero2} é: {resultado}")
elif operador == "/":
    try:
     resultado = numero1 / numero2
     print(f"O resultado de {numero1} dividido por {numero2} é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é possível.")
else:
    print("Operador inválido. Por favor, use +, -, * ou /.")