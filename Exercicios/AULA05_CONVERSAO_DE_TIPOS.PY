# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool = IMUTAVEIS
print(1 + 2)
print('a' + 'b')
print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 4) #converto str para int
print(float('1.2') + 5) #converto str para float
print(bool('1')) #converto str en bool retorna true 
print(bool('')) #str vazia retorna false
print(str('11') + "b") #converto int em str