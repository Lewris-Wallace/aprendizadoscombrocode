# Jogo Jokenpo
import random
lista = ["tesoura", "pedra", "papel"]

vitorias = 0
chances = 6

print('Sejam bem-vindos ao jogo de pedra, papel e tesoura!')
print('-' * 20)
print('Regras:\n' \
     '- Você terá 6 chances para o jogo em si e conquiste pelo menos 3 vitórias;\n' \
     "- Digite apenas 'pedra', 'papel' e 'tesoura', caso digite algum caractere inválido, o jogo não prosseguirá. ")
print('-' * 20)

while True:
     cavalo = input("Digite pedra, papel ou tesoura para disputar com um bot AI, para você conseguir ganhar dele: ")
     bot = random.choice(lista)
     
     if cavalo not in ['papel',  'pedra',  'tesoura']:
           print('-' * 20)
           print("Digite apenas pedra, papel e tesoura. Valor inválido.")
           print('-' * 20)
           continue

     print(f"Você colocou: {cavalo}")
     print(f"O bot colocou: {bot}")

     chances -= 1
     
     if cavalo == 'tesoura' and bot == 'papel':
          print('VOCÊ GANHOU!')
          vitorias += 1

     elif cavalo == bot:
          print(f"EMPATE! Não será contabilizado como vitória, mas você ainda tem {chances} chances")

     elif cavalo == 'pedra' and bot == 'tesoura':
          print('VOCÊ GANHOU!')
          vitorias += 1

     elif cavalo == 'papel' and bot == 'pedra':
          print('VOCÊ GANHOU!')
          vitorias += 1 
     
     else:
          print(f'VOCÊ PERDEU! Mas você ainda tem {chances} chances, tente conquistar a meta de 3 vitórias!')

     if chances == 0 and vitorias < 3:
              print(f"Você perdeu, com 6 chances, você conquistou {vitorias} vitórias, tente na próxima!")
              break

     if vitorias == 3:
              print(f"Parabéns!! Você conseguiu! Você venceu o jogo, restando {chances} chances")
              break

     