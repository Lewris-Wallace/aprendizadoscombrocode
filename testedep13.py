lista = ["doce", "amargo", "azedo", "salgado"] # Lista por colchetes
lista2 = {"doce", "amargo", "azedo", "salgado"} # Lista por chaves, mesmo se tiver duplicatas, ainda sim será considerado um valor só.
lista3 = ("doce", "amargo", "azedo", "salgado") # Lista por parênteses


# print(lista[0])

for x in lista:
    print(x)
print('-' * 30)

print(dir(lista))
print('-' * 30)

print(len(lista)) # A função "len" basicamente traz quantos valores têm dentro de uma variável, um exemplo é que na lista tem 4 valores.
print('-' * 30)

print("amargo" in lista) 
print("loucura" in lista) # Ambas as funções mostram o comando "in" para visualizar se na variável "lista" possui tal valor e é True ou False.
print('-' * 30)

adicionando = lista.append('desgosto')
print(lista) # O append basicamente adiciona um valor no final de uma lista.
print('-' * 30)

removendo = lista.remove('azedo')
print(lista) # Autoexplicativo, remove um valor dentro da lista.
print('-' * 30)

inserindo = lista.insert(1, 'raivoso')
print(lista) # O insert existe um parâmetro, o primeiro você vai indexar aonde ele vai ficar posicionado, se eu escolhi 1, 
# ele vai ficar atrás do "amargo", e o segundo, qual é o termo que você gostaria de adicionar
print('-' * 30)

ordenar = lista.sort()
print(lista) # Ordena por ordem alfabética, e do menor ao maior para ordem númerica
print('-' * 30)

reversao = lista.reverse()
print(lista) # Reverte a lista.
print('-' * 30)

print(lista.index("raivoso")) # Retorna o número do index da lista, nesse exemplo seria o 1, que o raivoso está na segunda posição.
print('-' * 30)

print(lista.count("amargo")) # Retorna o número exato de termos "amargo" dentro do terminal, ou seja, nesse caso seria 1, porque 
# só existe um termo chamado amargo
print('-' * 30)
# Abaixo agora será utilizado o conceito de chaves, e tudo acima é utilizando a lista em colchetes
# ---
print(lista2)
print('-' * 30)

print(dir(lista2))
print('-' * 30)
# print(lista2[1]) (Utilizar a indexação dentro de chaves, é impossível, pois não existe uma ordenação exata quando os valores estão em chaves.)

print(lista2.add('cavalo'), lista2) # Adição de um elemento
print('-' * 30)

loucuradois = lista2.pop()
print(lista2) # Tira um elemento e deixa em ordem aleatória
print('-' * 30)

limpeza= lista2.clear()
print(lista2) # Limpa a quantidade de elemntos
print('-' * 30)

adicao2 = lista2.add('teste')
print(lista2) # Para provar a limpeza feita com o comando clear, utilizei o "add" para adicionar um novo elemnto e começar 
# com um outro elemento na lista com chaves
print('-' * 30)