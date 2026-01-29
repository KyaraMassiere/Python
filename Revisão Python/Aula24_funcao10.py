def verificar_voto(idade):
    if idade <16:
        return "Não vota"
    elif idade >=16 and idade <18:
        return "Voto Opcional"
    elif idade >=18 and idade <=70:
        return "Voto obrigatorio"
    elif idade >70:
        return "Voto opcional"

idade = int(input("Qual a sua idade? "))
situacao_voto = verificar_voto(idade)
print(f"Com a idade {idade} anos, a situação é {situacao_voto}")