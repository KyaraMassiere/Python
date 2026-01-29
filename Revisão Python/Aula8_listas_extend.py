mochila = ["notebook","garrafa","mouse"]
novos_itens = ["estojo","borracha","celular"]
mochila.extend(novos_itens)
for item in mochila:
    print(f"-{item}")