tradutor = {
    'perro': 'cachorro',
    'rojo':'vermelho',
    'si': 'sim',
    'hola': 'oi',
    'buceo': 'mergulho'
}
while True:
    escolha = input("Qual a palavra em espanhol quer traduzir? ")
    if escolha == 'sair':
        break
    if escolha in tradutor:
        significado = tradutor[escolha]
        print(f'A tradução da palavra é {significado}')
    else:
        print(f'Esta palavra eu não sei')
        ensinar = input(f"Como se diz {escolha} em português? ")
        tradutor[escolha] = ensinar
        print(f'Aprendido! Palavra adicionada ao dicionário')

for original, traducao in tradutor.items():
    print(f'Espanhol: {original} | Português: {traducao}')