inicio = 24
fim = 24
while inicio > 23 or fim > 23:
    inicio = int(input("inicio do jogo:"))
    fim = int(input("fim do jogo:"))
    if inicio > 23 or fim > 23:
        print("horário maior que 24 horas")
    else:
        if inicio < fim:
            tempo = fim - inicio
            print("O tempo de partida foi:", tempo,"horas")
        elif inicio > fim:
            temp1 = 24 - inicio
            tempo = fim + temp1
            print("O tempo de partida foi:", tempo,"horas")
        elif inicio == fim:
            print("O tempo de partida foi de 24 horas")
