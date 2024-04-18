# Dicionarios 

elemento = { 
    'Z': 3,
    'nome': 'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534     

}

print(f'elemento:  {elemento["nome"]}')
print(f'denssidade:  {elemento["densidade"]}')
print(f'o dicionário possui:  {len(elemento)} elementos.')

# Atualizar uma entrada

elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['perido'] = 1
print(elemento)

# # excluação de itens do dicionário
# del elemento['perido']
# print(elemento)

# # limpar e apagar todos os itens
# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)

# #verificando todos e itens e usando o for
# print(elemento.items())
# for i in elemento.items():
#     print(i)

#Verificando somente as chaves do dicionário
print(elemento.keys())
for i in elemento.keys():
     print(i)
#Verificando somente as valores do dicionário
print(elemento.values())
for i in elemento.values():
     print(i)
for i, j in elemento.items():
     print(f'{i}:{j}')
     
