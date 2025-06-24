# Operação aritmética

adicao = 10 + 10
print("Adicao", adicao)

subtracao = 10 - 5
print("Subtracao", subtracao)

multiplicacao = 10 * 5
print("Multiplicacao", multiplicacao)

divisao = 10 / 5
print("Divisao", divisao)

modulo = 10 % 3
print("Modulo", modulo)

exponenciacao = 10 ** 2
print("Exponenciacao", exponenciacao)

divisao_inteira = 10 // 3
print("Divisao Inteira", divisao_inteira)

# Podemos usar "+" para concatenar strings
concatenacao = "Ducher" + " " + "M Seidi"
print(concatenacao)

# Podemos usar "*" para repetir strings
repeticao = "Ducher " * 3
print(repeticao)

# Precendencia de operadores
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*)  Divisão (/) Modulo (%) e Divisão Inteira (//)
# 4. Adição (+) e Subtração (-)
resultado = (10 + 5) * (2 - 3) / 1 ** 2
print("Resultado", resultado)

# Exercício para calcular IMC (Índice de Massa Corporal)
peso = 80
altura = 1.92
nome = "Ducher M Seidi"
imc = peso / (altura ** 2)
print(f"{nome} tem {altura} de altura, pesa {peso} kg e seu IMC é {imc}")