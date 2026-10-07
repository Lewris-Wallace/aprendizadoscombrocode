senha = input("Digite uma senha forte: ")


print(senha.find(" "))

if len(senha) < 8:
    print("Senha fraca: deve ter pelo menos 8 caracteres.")
elif not senha.find(" ") == -1:
    print("Senha fraca: não deve conter espaços.")
elif senha.isalpha():
    print("Senha fraca: deve conter pelo menos um número.")
else:
    print("Senha forte: atende aos critérios de segurança.")
