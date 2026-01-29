def calcular_media(nota1, nota2):
    media = (nota1 + nota2) /2
    return media 
medias = []
for i in range(3):
    nota1 = float(input("Qual a primeira nota do aluno? "))
    nota2 = float(input("Qual a segunda nota do aluno? "))
    media_final = calcular_media(nota1,nota2)
    medias.append(media_final)
    print(f"Média registrada, media final {media_final}")

print(f"Todas as medias: {medias}")
campeao = max(medias)
print(f"A maior media da turma foi {campeao}")

