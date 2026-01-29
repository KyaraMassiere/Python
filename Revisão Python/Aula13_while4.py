numero_secreto = 7
chute = int(input("Qual o numero secreto?"))
while chute != numero_secreto:
    print("Errou! Tente novamente")
    chute = int(input("Qual o numero secreto?"))
print("Parabéns você acertou o número secreto!")