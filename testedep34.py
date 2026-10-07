# Mini projeto de banco em Python


def mostrar_conta(conta):
    print("*" * 30)
    print(f"Na sua atual conta, você possui: R$ {conta:.2f}")
    print("*" * 30)

def depositar(conta):
    while True:
        try:
            valor = float(input("Digite o valor a ser depositado: R$ "))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            conta += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    return conta

def saque(conta):
    while True:
        try:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue
            if valor > conta:
                print("Saldo insuficiente. Tente novamente.")
                continue
            conta -= valor
            print("*" * 30)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    return conta

if __name__ == "__main__":
    print("Bem-vindo ao Mini Banco!")
    print("*" * 30)
    conta = 0

    while True:
      print("Escolha uma opção:")
      print("1. Mostrar saldo")
      print("2. Depositar")
      print("3. Sacar")
      print("4. Sair")
      print("*" * 30)

      opcao = input("Digite o número da opção desejada: ")

      if opcao == "1":
        mostrar_conta(conta)
      elif opcao == "2":
        conta = depositar(conta)
      elif opcao == "3":
        conta = saque(conta)
      elif opcao == "4":
        print("Saindo do programa. Até logo!")
        break
      else:
        print("Opção inválida. Tente novamente.")