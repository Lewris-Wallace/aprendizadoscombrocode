# Sobre dicionários:

capitais = {"Brasil": "Brasília",
            "Espanha": "Madrid",
            "Inglaterra": "Londres",
            "Estados Unidos": "Washginton"}

print(capitais.get("Brasil")) # Em outras palavras, ele pega o valor que é conservado do termo 'Brasil', trazendo o resultado de Brasília.

if capitais.get('Espanha'):
    print('Essa capital existe!')
else:
    print('Essa capital não existe.')

print('-' * 30)

atualizacao = capitais.update({"Brasil": "Rio de Janeiro"}) # Mudança do dicionário de Brasil para RJ
print(capitais.get("Brasil"))
print('-' * 30)

print(capitais)
print(capitais.pop("Estados Unidos"))
print(capitais, "| Os Estados Unidos foi retirado.")
print('-' * 30)

print(capitais.popitem()) # Exclui o dicionário mais recente, nesse caso seria a Inglaterra.
print(capitais)
print('-' * 30)

chaves = capitais.keys()
valores = capitais.values()
itens = capitais.items()

print(chaves) # Aqui fala quais são as chaves dominantes do dicionário montado lá encima.
print(valores) # Aqui são os valores guardados dentro das chaves.
print(itens) # Aqui retorna os valores das chaves e dos valores em si.
print('-' * 30)

for chave, valor in itens:
    print(f'{chave}: {valor}')