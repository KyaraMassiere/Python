"""
 Formatação básica de strings
 s - string
 d - int
 f - float
 .<número de dígitos>f
 x ou X - Hexadecimal
 (Caractere)(><^)(quantidade)
 > - Esquerda
 < - Direita
 ^ - Centro
 = - Força o número a aparecer antes dos zeros
 Sinal - + ou -
 Ex.: 0>-100,.1f
 Conversion flags - !r !s !a 
 """
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #VAI DAR 10 ESPAÇOS A DIREITA
print(f'{variavel: <10}.')# VAI DAR 10 ESPAÇOS A ESQUERDA
print(f'{variavel: ^10}.')#PARA CENTRALIZAR
print(f'{1000.4873648123746:0=+10,.1f}')#APENAS UMA CASA DECIMAL
print(f'O hexadecimal de 1500 é {1500:08X}')# X PARA HEXADECIMAL
print(f'{variavel!r}')