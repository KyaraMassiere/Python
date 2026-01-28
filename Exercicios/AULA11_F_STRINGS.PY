"""nome = 'Ana Maria'
altura = 1.80
peso = 95
imc = peso / altura ** 2
print(imc)"""

#resultado deu certo 29.3209876...

nome = "Kyara"
altura = 1.67
peso = 84
imc = peso / altura **2
linha_1 = f'{nome} tem {altura} metros de altura, e seu imc é {imc}'
print(linha_1)
linha_2 = f'{nome} tem {altura:.2f} metros de altura, e seu imc é {imc:.3f}'
#al colocar :.2f na altura estou definindo a quantidade de casas decimais
print(linha_2)