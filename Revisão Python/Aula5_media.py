prova1 = float(input("Qual a nota da prova1?"))
prova2 = float(input("Qual a nota da prova2?"))
trabalho = float(input("Qual a nota do trabalho em grupo?"))

mediageral = (prova1 + prova2 + trabalho) /3
if mediageral>=6:
    print(f"Aluno aprovado com a media: {mediageral:.2f}")
else:
    print(f"Aluno reprovado com a media: {mediageral:.2f}")