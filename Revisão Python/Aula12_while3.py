opcao =""
while opcao != "3":
    print("\n-----Menu do Banco-----")
    print("1. Ver Saldo")
    print("2. Fazer depósito")
    print("3. Sair")

    opcao = input("Escolha uma opção do menu: ")
    if opcao == "1":
        print("Seu saldo é de 500,00")
    elif opcao == "2":
        print("Depósito realizado com sucesso")
    elif opcao == "3":
        print("Saindo do sistema...Obrigada por ultilizar nossos serviços")
    else:
        print("Opção invalida, tente novamente 1, 2 ou 3")
print("Volte sempre")

