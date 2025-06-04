conta = int(input("digite a sua conta:"))
saldo = int(input("digite o seu saldo:"))
debito = int(input("digite o seu débito:"))
credito = int(input("digite o seu crédito:"))
saldoatual = saldo - debito + credito
if saldoatual > 0:
    print("seu saldo é positivo: R$", saldoatual)
elif saldoatual < 0:
    print("seu saldo é negativo: R$", saldoatual)
else:
    print("Você está zerado")
