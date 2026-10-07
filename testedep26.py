def adicionar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(adicionar(1, 3, 5, 7))
print('-' * 40)
# Os kwargs (**[nomedoparametro]) são direcionados como dicionários, ou seja, qualquer operação com Python
# relacionado a eles, você precisa ter ciência que está lidando com um tipo de dicionário.
def nome_completo(**nomes): 
    for chave, valor in nomes.items():
        print(f"{chave.capitalize()}: {valor}")

nome_completo(nome="Seu Barriga", 
              sobrenome="da Costa Leste", 
              utlimonome="de Vicente Júnior")

print('-' * 40)

def quantoqueelegastou(*nome, **meses):
    print(f"Olá, {nome[0]}, veja seus gastos!")
    for mes, valor in meses.items():
        print(f"No mês de {mes}, você gastou {valor:.2f} R$")

quantoqueelegastou("Samuel Soares",
                   janeiro=555,
                   fevereiro=235,
                   marco=220,
                   abril=123,
                   maio=2345,
                   junho=1355)
    
    