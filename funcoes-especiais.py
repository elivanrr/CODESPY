## Funções lambda (Anônimas) ou únicas
# Sintaxe:
#Lambda argumentos: expressão

# quadrado = lambda x: x**2

# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0  # usando uma função lambda para saber se o numero e par
# print(par(8))

# f_c = lambda f: (f - 32) * 5/9   # usando a funação lambda para converter o temperatuara firehard e celcus 
# print (f_c(32))

## Funça map() função que aplica função
# Sintaxe
# map(funçao, iteravel) de rordem superior e de programação funcional

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))   # Aqui se usa a função list para converte o objeto da função map em lista e usa 
# print(dobro)                                        # função lanbda para relaiza o calculo do dobro de num da lista 

# palavras = ['ehf', 'consultoria', 'em ti'] # Agor uando p map sobre stringo usando a função str upper.
# maiuscula = list(map(str.upper, palavras))
# print(maiuscula)

## Função filter()
# sintaxe:
#filtter(função, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_par = list(filter(numeros_pares, numeros)) # Aqui o filter e aplicado extraindo os numeros pares da lista que 
# print(num_par)                                                #foi submetida a função def

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# num_impar = list(filter(lambda x: x %2 != 0, numeros ))
# print(num_impar)


# Função reduce()  retorna o valor total de forma unica da sequencia cumulativa e é preciso importa ela da functools
# Sintaxe 
# reduce (função, sequência, valor_inicial)
# from functools import reduce

# def mult(x, y):
#     return x * y
# numeros = [1,2,3,4,8,6]

# total = reduce(mult, numeros )
# print(total)

# usando o reduce e lambda soma cumulativa dos quadrados de valores.
# Ex: ((1²+2²)² + 3²)² + 4²

from functools import reduce
numeros = [1,2,3,4]
total = reduce(lambda x, y: x**2 + y**2, numeros)
print(total)








