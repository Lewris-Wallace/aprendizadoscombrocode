def feliz_aniversario(nome, idade):
    print("É pique, é pique")
    print("É hora, a thi")
    print("HUUUUUUUU")
    print(f"{nome}, {nome}, {nome}")
    print(f"Parabéns a {nome}, que está fazendo {idade}")
    
    
feliz_aniversario("Samuel", 17)

def vencer_fatura(nome, valor, vencimento):
    print(f"Olá, {nome}, sua fatura é de {valor:.2f} e o seu vencimento é de: {vencimento}")

vencer_fatura("Samuel", 200, "30/12/2027")





def somar(numero1, numero2):
    numero3 = numero1 + numero2
    return numero3

def subtracao(numero1, numero2):
    numero3 = numero1 - numero2
    return numero3

print(somar(2, 3))
print(subtracao(5, 3))


def nome_completo(primeiro_nome, segundo_nome):
    print(f"Seu nome completo é: {primeiro_nome.capitalize()}", f"{segundo_nome.capitalize()}")

nome_completo("samuel", "soares")