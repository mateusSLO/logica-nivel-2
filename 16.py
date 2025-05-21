nota1 = int(input("Nota primeiro semestre:"))
nota2 = int(input("Nota segundo semestre:"))
nota3 = (nota1 + nota2) / 2
if nota3 >= 6:
    result = "aprovado"
else:
    result = "reprovado"
print("O aluno foi",result,"com a média", nota3)
