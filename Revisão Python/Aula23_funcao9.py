def resultado_imc(imc):
    if imc <25:
        return "Peso normal"
    elif imc >25 and imc <30:
        return "Sobrepeso"
    else:
        return "Obeso"

peso = float(input("Qual o peso do paciente? "))
altura = float(input("Qual a altura do paciente? "))
imc = peso / altura ** 2
imc_final = resultado_imc(imc)
print(f"Seu imc final é {imc:.2f} e sua categoria é {imc_final}")

    