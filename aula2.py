# conversão de tipos, coerção
# é ato de converter um tipo de dado em outro tipos imutáveis e primitivos:
# str, int, float, bool

print(10 + 5)  # Soma dois números inteiros
print(10 - 5)  # Subtrai dois números inteiros
print(10 * 5)  # Multiplica dois números inteiros
print(10 / 5)  # Divide dois números inteiros
print(10 // 3)  # Divisão inteira, resultado é o quociente sem o resto
print(10 % 3)  # Módulo, resultado é o resto da divisão
print(10 ** 3)  # Exponenciação, resultado é 10 elevado a 3
print('a' + 'b')  # Concatena duas strings, resultado é 'ab'

# converter
print(int('1'), type(int('1')))  # Converte string '1' para inteiro
print(int('1') + 1)  # Soma 1 ao inteiro convertido, resultado é 2
print(float('1'))  # Converte string '1' para float
print(str(11) + 'b')  # Converte inteiro 11 para string e concatena com 'b', resultado é '11b'
print(bool(' '))  # Converte inteiro 1 para booleano, resultado é True