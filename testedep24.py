# def prever_desconto(preco, desconto=0, taxa=0.05):
#     return preco * (1 - desconto) * (1 - taxa)

# print(prever_desconto(200))

import time
# Argumentos padrão dentro dos parâmetros do def (função), é quando existe já um valor que é definido inicialmente, nesse caso, 
# o parâmetro 'comeco' é definido comumente como sempre 0, mas pode ser alterado, dependendo da escolha do usuário dentro dos argumentos.
def contagem(fim, comeco=0):
    for contando in range(comeco, fim+1):
        print(contando)
        time.sleep(1)
    print("Contagem finalizada!")

contagem(10, 5)
