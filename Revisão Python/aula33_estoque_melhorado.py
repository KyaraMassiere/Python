estoque = {
    'tomate': 10,
    'alface': 5,
    'batata': 20
}
def listar_estoque():
    print(f'\n------Estoque Atual Atualizado------')
    for original, quantidade in estoque.items():
        print(f'Produto: {original} | Quantidade: {quantidade}')
        print(f'--------------------------------------')

while True:
    listar_estoque()
    produto = input('Qual o produto deve ser gerenciado? ')
    if produto == 'sair':
        print(f'Saindo do sistema...')
        break
    elif produto in estoque:
        del estoque[produto]
        print('Produto deletado com sucesso')
    else:
        print(f'Este produto não está no estoque')
        criar = input(f'Gostaria de cadastrar {produto} no estoque (s/n)? ')
        if criar == 's':
            estoque[produto] = int(input(f'Qual a quantidade {produto}? '))
            print(f'Novo produto adicionado com sucesso!')
        elif criar == 'n':
            print('Produto não cadastrado')
