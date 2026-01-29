def situaçao(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

nota = float(input("Qual a nota?"))
veredito = situaçao(nota)
print(f"O aluno está {veredito}")