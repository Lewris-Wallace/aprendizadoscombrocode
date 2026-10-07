# Projeto de Caça-Níquel em Python (bet)
import random
import time

def apostando():
    simbolos = ["🍒", "🍋", "🍊", "🍉", "⭐"]

    return [random.choice(simbolos) for _ in range(3)]

def pagamento(resultado, aposta):
    if resultado[0] == resultado[1] == resultado[2]:
        simbolo = resultado[0]
        multiplicadores = {
            "🍒": 3,
            "🍋": 5,
            "🍊": 8,
            "🍉": 10,
            "⭐": 20
        }
        return aposta * multiplicadores[simbolo]
    else:
        return 0


def main():
    conta = 100
 
    print("Bem-vindo ao Caça-Níquel!")
    print("Símbolos disponíveis: 🍒, 🍋, 🍊, 🍉, ⭐")
    print("*" * 30)
    print("Regras: \n - A aposta mínima é de R$ 1 real; \n - Se você acertar 3 símbolos iguais, você ganhará uma premiação;"
    "\n - Cada símbolo terá um multiplicador diferente do dinheiro apostado; \n "
    "- Se você não acertar 3 símbolos iguais, você perderá o valor apostado.")
    print("*" * 30)
    print(f"Multiplicadores por símbolo: \n - 🍒: 3x; \n - 🍋: 5x; \n - 🍊: 8x; \n - 🍉: 10x; \n - ⭐: 20x")

    while conta > 0:
        print(f"Saldo atual: R$ {conta:.2f}")
        print('*' * 30)

        
        aposta = input("Digite o valor da aposta (ou 'sair' para encerrar): ")
        if aposta.lower() == 'sair':
            print(f"Obrigado por jogar! Seu valor total foi de R$ {conta:.2f}. Até a próxima.")
            break

        if not aposta.isdigit() or int(aposta) <= 0:
            print("Valor inválido. Por favor, digite um número positivo.")
            continue

        resultado = apostando()
        aposta = int(aposta)

        if aposta > conta:
            print("Saldo insuficiente para essa aposta. Tente novamente.")
            continue

        if aposta < 1:
            print("A aposta mínima é de R$ 1 real. Tente novamente.")
            continue

        if conta >= 1:
           print("Girando os slots...")
           time.sleep(1.5)
           print(f"Resultado do jogo: {' | '.join(resultado)}")
           conta -= aposta
           if resultado[0] == resultado[1] == resultado[2]:
               ganho = pagamento(resultado, aposta)
               conta += ganho
               print(f"Parabéns! Você ganhou R$ {ganho:.2f}!")
           else:
               print("Que pena! Você não acertou 3 símbolos iguais. Tente novamente.")


        if conta < 1 and conta >= 0:
            print('*' * 30)
            print("Você faliu! O saldo da sua conta é insuficiente para continuar jogando. Obrigado por jogar! Até a próxima.")

if __name__ == "__main__":
    main()

# Continuar depois