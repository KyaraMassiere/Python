def calcular(altura, comprimento):
    area = altura * comprimento 
    return area

altura = float(input("Qual a altura do terreno? "))
comprimento = float(input("Qual o comprimento do terreno? "))
resultado = calcular(altura, comprimento)
print(f"A area do terreno é {resultado}")