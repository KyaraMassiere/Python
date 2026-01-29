senha_secreta ="1234"
tentativa = input("Qual é a senha?")

while tentativa != senha_secreta:
    tentativa = input("Senha incorreta. Digite novamente a senha: ")
print("Acesso liberado")