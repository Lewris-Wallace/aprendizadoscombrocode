
def definir_dia(dias):
    match dias:
        case 1:
            print("Hoje é segunda-feira!")
        case 2:
            print("Hoje é terça-feira!")
        case 3:
            print("Hoje é quarta-feira!")
        case 4:
            print("Hoje é quinta-feira!")
        case 5:
            print("Hoje é sexta-feira!")
        case 6:
            print("Hoje é sábado!")
        case 7:
            print("Hoje é domingo!")
        case _:
            print("Dia não válido")

definir_dia(2)

def definir_finaldesemana(semana):
    match semana:
        case "Segunda-Feira" | "Segunda" | "segunda":
            print('Segunda-feira não é dia de semana.')
        case "Terça-Feira" | "Terça" | "terça": 
            print("Terça-feira não é dia de fim de semana.")
        case "Quarta-Feira" | "Quarta" | "quarta": 
            print("Quarta-feira não é dia de fim de semana")
        case "Quinta-Feira" | "Quinta" | "quinta": 
            print("Quinta-feira não é dia de fim de semana.")
        case "Sexta-Feira" | "Sexta" | "sexta": 
            print("Sexta-feira não é dia de fim de semana.")
        case "Sábado" | "sabado" | "sábado": 
            print("Sábado é dia de fim de semana!")
        case "Domingo" | "domingo": 
            print("Domingo é dia de fim de semana!")
        case _: print("Dia não válido.")


definir_finaldesemana("Segunda")