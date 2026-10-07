lista = ("sabão", "coco", "laranja", "doideira")
lista2 = {"sabão", "coco", "laranja", "doideira"}

for listas in reversed(lista):
    print(listas)
# O primeiro irá ter assertividade em execução, pois a lista em si está em uma tupla, ou seja, em parênteses
for listas3 in reversed(lista2):
    print(listas3)
# Aqui não funcionará, pois aqui a lista está em chaves, tendo até mesmo um erro quando for executado, quando a lista está em chaves, 
# o posicionamento não pode ser alterado.