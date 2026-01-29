def checar_febre(temperatura):
    if temperatura >= 37.5:
        return "febril"
    else:
        return "com temperatura normal"

temperatura = float(input("Qual a temperatura do paciente? "))
diagnostico = checar_febre(temperatura)
print(f"O paciente está {diagnostico}")