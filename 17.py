ano1 = int(input("Qual o ano atual?"))
ano2 = int(input("Qual o ano de nascimento?"))
ano3 = ano1 - ano2
if ano3 >= 18:
    print("Pode votar")
else:
    print("Não pode votar")
