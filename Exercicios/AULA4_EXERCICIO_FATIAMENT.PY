"""
 Exercício
 Peça ao usuário para digitar seu nome
 Peça ao usuário para digitar sua idade
 Se nome e idade forem digitados:
     Exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Seu nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A última letra do seu nome é {letra}
 Se nada for digitado em nome ou idade: 
     exiba "Desculpe, você deixou campos vazios."
 """
"""nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Verifica se nome e idade não estão vazios
if nome and idade:
    # Usando f-strings e fatiamento
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome contém {' ' in nome and 'contém' or 'não contém'} espaços")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    # Caso nome ou idade estejam vazios
    print("Desculpe, você deixou campos vazios.")"""

nome = input("digite seu nome: ")
idade = input('digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"seu nome tem {len(nome)} letras")
    print(f"Seu nome {' ' in nome and "contém" or "não comtém"} espaços")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou os campos vazios")




