# Lições de funções:

def funcao1():
    x = 10
    def funcao2():
        print(x)
    funcao2()
x = 20 # Percebe-se que quando eu chamo a função 1, ela vai imprimir o valor de x que está dentro dela, e não o valor de x que está fora dela, 
# ou seja, o valor de x que está dentro da função 1 tem prioridade sobre o valor de x que está fora da função 1.

def funcao3():
    print(x) # O valor de x dentro da função 3 não existe prioridade nenhuma, mas quando atribuímos um valor fora da função, 
# no caso, abaixo que é o valor 20, ele será impresso, 
# pois o valor de x que está fora da função 3 tem prioridade sobre o valor de x que está dentro da função 3, que não existe.
x = 20
funcao3()
print('-' * 20)
funcao1() # Aqui eu chamo a função 1, que por sua vez chama a função 2, e a função 2 imprime o valor de x, que é 10
