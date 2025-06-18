# Permite escrever um comentário, e funciona para uma linha que vai ignorar o texto deois de cardinal

"""
Aqui você pode escrever frase ou paragrafos inteiros, usando três aspas duplas.
"""
# sep significa separador, e end significa o que vai ser impresso no final da mensagem
print(34, 23, sep= '-', end='\n')  # Imprime uma mensagem na tela, e podemos ter vários argumentos separados por vírgula

"""
Python = linguagem de programação
Tipo de tipagem = Dinâmica /  Forte
str = string (texto dentro de aspas simples ou duplas)
int =  inteiro (núimero inteiro)
float = ponto flutuante (número com vígula)
bool = booleano (verdadeiro ou falso)
"""

#############################String###########################################

# Aspas simples e duplas podem ser usadas para definir strings
print("1.Olá, mundo!")  
print('2.Olá, mundo!', 'Python é legal!')  # Imprime várias mensagens na tela, separadas por vírgula

# Escape de caracteres
print("1.Olá, mundo! \"Python é legal!\"")  #  Imprime uma mensagem na tela, com aspas duplas dentro da string
print('2.Olá, mundo! "Python é legal!"')

# r
print(r"Olá, mundo! \"Python é legal!\"")  # Imprime uma mensagem na tela, com r antes da string para tratar como raw string, imprimir \ também

#############################Inteiro e Float################################

num_int = 10 # Definindo um número inteiro
num_int2 = -20
print(num_int + num_int2)  # Imprime a soma de dois números inteiros na tela
num_float = 10.5  # Definindo um número float
print(num_float)  # Imprime o número inteiro na tela

# A função type mostra o tipo que o Python
# inferiu ao valor
print(  type(20)) # imprime o tipo de objeto

########################Booleano#####################################
# questiona se valor é verdadeiro ou falso (True ou False)
print(1 > 5)  # Imprime True, pois 10 é maior que 5
print(10 == 10)  # Imprime True, pois 10 é igual a 10