def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Qual o seu peso em kg? "))
altura = float(input("Qual a sua altura em metros? "))
resultado_imc = calcular_imc(peso, altura)
print(f"O imc do paciente é de {resultado_imc:.2f}")