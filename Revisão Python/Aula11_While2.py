nota = float(input("Digite a nota do aluno (0 a 10): "))
while nota <0 or nota >10:
    print("Erro! A nota deve ser entre 0 e 10")
    nota = float(input(("Tente novamente. Digite a nota (0-10) novamente: ")))
print(f"Nota registrada {nota}")