import time

questoes = ("1. Qual é o valor total de QI de um sapo?",
            "2. Quais são as probabilidades dos seus dedos ficarem azuis?",
            "3. Quem pintou a Monalisa?",
            "4. O que é o romantismo?"
)

opcoes = (("A. 113",  "B. 114",  "C. 115",  "D. O sapo não possui QI."),
          ("A. 2,5%",  "B. 100%",  "C. 0.72%",  "D. 66%."),
          ("A. Leonardo da Vinci", "B. Pablo Picasso",  "C. Abobaleda Romeu",  "D. Rembrandt van Rijn"),
          ("A. Surgiu na Itália.",  "B. Valorizava a razão.",  "C. Rejeitava emoções.",  "D. Valorizava sentimentos."))

respostas = ("D", "A", "A", "D")
perguntas = []
numero_questao = 0
acertos = 0

for questao in questoes:
    print('-------------------')
    print(questao)
    for opcao in opcoes[numero_questao]:

        print(opcao)
    print('-------------------')
    while True:
     pergunta = input("Qual é a letra correta nesse quesito? ").upper()

     if pergunta not in ["A", "B", "C", "D"]:
        print("Inválido! Digite letras de A, B, C ou D.")
        continue
    
     if pergunta == respostas[numero_questao] and pergunta in ["A", "B", "C", "D"]:
        perguntas.append(pergunta)
        print('--------------------')
        print("Analisando..")
        time.sleep(1.5)
        print('Uou, você acertou!')
        acertos +=1
        break
     else:
        print('-------------------')
        print("Analisando..")
        time.sleep(1.5)
        print("Infelizmente, você errou..")
        print(f"A correta é a {respostas[numero_questao]} ")
        perguntas.append(pergunta)
        break
    numero_questao += 1

print('-' * 30)
print('RESULTADOS:')
print('-' * 30)
print('Você respondeu tais questões com as seguinte alternativas:', end=' ')
print(*perguntas, sep=" | ")
print(f'E esses são as respostas corretas: {respostas}')

# Você posteriormente vai invalidar todas essas questões