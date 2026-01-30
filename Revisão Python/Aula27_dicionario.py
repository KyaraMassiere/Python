tradutor = {
    'perro': 'cachorro',
    'rojo':'vermelho',
    'si': 'sim',
    'hola': 'oi',
    'buceo': 'mergulho'
}
escolha = input("Qual a palavra em espanhol quer traduzir?")
if escolha in tradutor:
    significado = tradutor[escolha]
    print(f'A tradução da palavra é {significado}')
else:
    print(f'Esta palavra não existe no dicionario atual')