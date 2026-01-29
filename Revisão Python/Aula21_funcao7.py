def dividir_conta(valor_total, pessoas):
    conta = valor_total / pessoas
    return conta

valor_total = float(input("Qual o valor total da conta? "))
pessoas = int(input("Qual o numero de pessoas? "))
conta_pessoa = dividir_conta(valor_total, pessoas)
print(f"O valor total por pessoa é {conta_pessoa:.2f}")