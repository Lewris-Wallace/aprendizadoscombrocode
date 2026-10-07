# Validor de cartão de crédito

numeros_do_cartao = 0
numerospares = 0
total = 0 

while True:
  numero_cartao = input("Digite o número do cartão de crédito: ")
  numero_cartao = numero_cartao.replace(" ", "").replace("-", "")

  if numero_cartao.isdigit() and len(numero_cartao) == 16:
   print("Número do cartão de crédito:", numero_cartao)
   break
  else:
   print("Número do cartão de crédito inválido. Digite novamente.")
   continue