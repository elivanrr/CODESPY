# nome = 'Elivan'
# letra = nome[2]
# print(letra)
# print(len(nome))

# nome = 'Curso de python'
# aluno = 'Elivan'
# print( nome + ' é  o ' + aluno)

#frase =  'Vamos aprender python hoje.'
#palavras = frase.split()
# print(palavras)
# print(palavras[1])
# for palavra in palavras:
#     print(palavra)
# for letra in frase:
#     print(letra)
#print(frase[6:15])  # usando slace

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@') # Pesquisando um carctere dentro das strings
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(f'Nome do Usuário: {usuario} e o Dominio : {dominio}')

# produtos = 'Carbonato de sódio e oxído de zinco'
# print('sódio' in produtos)
# print('magnesio' in produtos)
# print('magnesio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')   # o find não encontra o valor ele retorna -1
# print(pos)

# objeto_celeste = 'galaxia esPiral M31'
# print(objeto_celeste.upper()) # transforma em maiusculo 
# print(objeto_celeste.lower())  # transforma tudo minusculo
# print(objeto_celeste. capitalize()) # Primeira letra em maiusculo
# print(objeto_celeste.title()) # Começo de cada letra em maiusculo

# suplemento = 'cloreto de magnésio'
# n_sup = suplemento.replace('magnésio', 'zinco') # realiza a substituição das strnsg ou texto desejado
# print(n_sup)

# frase = '        ômega 3 é bom para saúde!     '
# print (frase.lstrip())  # o strip elimina e ajusta para direita, esquerda e certraliza o texto
# print (frase.rstrip())
# print (frase.strip())

# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20)) # inseri e ajusta o texto
# print(fruta.center(20))
# print(fruta.ljust(20, "-"))
# print(fruta.center(20, "-"))


# p = "ehf consultoria"
# print(p.startswith('eh')) # verifica com que caractere começa e termina
# print(p.startswith('Eh'))
# print(p.endswith('a'))
# print(p.endswith('o'))

# Docstrings documenta trecho dos codigos

texto = """
Docstrings é uma espécie de documentção 
que pedemos inserir dentro de módulo, função 
ou classes do python, entre outrtos locais.
    Respeita deslocamento do texto e é multilinhas
"""
print(texto)






