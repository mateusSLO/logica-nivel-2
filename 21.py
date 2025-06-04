cont = 4
somasal = 0
salario = int(input("digite o valor do salario:"))
while cont != 0:
    print("Digite as horas trabalhadas da", cont, "semana:")
    sal = int(input())
    if sal <= 40:
        sal1 = sal * salario
    else:
        sal1 = (40 * salario) + ((sal - 40)* (salario * 1.5))
    cont -= 1
    somasal += sal1
print("Seu salário deste mês ficou R$", somasal)
