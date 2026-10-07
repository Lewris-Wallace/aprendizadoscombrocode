email = input("Digite seu email: ")

index = email.index("@")

nome_usuario = email[:index]
nome_email = email[index + 1:]

print(f"O nome do usuário é: {nome_usuario} e o domínio do email é: {nome_email}")