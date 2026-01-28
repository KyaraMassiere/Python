numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 < numero2:
    print(f'Segundo valor {numero2} é maior que o primeiro valor {numero1}')
elif numero1 > numero2:
    print(f'Primeiro valor {numero1} é maior que o segundo valor {numero2}')
else:
    print(f'Primeiro valor {numero1} é igual ao segundo valor {numero2}')