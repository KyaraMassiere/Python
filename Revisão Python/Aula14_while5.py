total = 0.0
preço_do_produto = float(input("Digite o preço do produto (ou 0 para fechar a conta): "))
while preço_do_produto != 0:
    total = total + preço_do_produto
    preço_do_produto = float(input("Digite o preço do produto (ou 0 para fechar a conta): "))
print(f"Total a pagar {total:.2f}")