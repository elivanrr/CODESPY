# PS C:\Users\elivan.franco\Downloads\TEMPSFZ> py
# Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.name
# 'nt'
# >>> os.getcwd
# <built-in function getcwd>
# >>> os.getcwd()
# 'C:\\Users\\elivan.franco\\Downloads\\TEMPSFZ'
# >>> os.cudir
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'os' has no attribute 'cudir'. Did you mean: 'chdir'?
# >>> os.curdir
# '.'
# >>> list dir
#   File "<stdin>", line 1
#     list dir
#          ^^^
# SyntaxError: invalid syntax
# >>> os.listdir()
# os.chdir('c:\\')
# os.mkdir( )

# >>> pasta_nova = 'Teste2'
# >>> pasta_pai = 'c:\\'
# >>> caminho_completo = os,path(pasta_pai, pasta_nos)
# >>> os.rename('C:\\Teste2', 'C:\\Teste10') 
# >>> os.rmdir('C:\\Teste2', 'C:\\Teste10') apaga 

# Criando muitas pastas
#>>> pasta_pai = os.getcwd()
#>>> novas_pastas  = 'America\\Brasil\\Ilhabela'
#>>> caminho = os.path.join(pasta_pai, novas_pastas)
#>>> print(caminho) 
#>>> os.makedirs(caminho)  # Utilizando (caminho, modo) será tratado as permissões, tendo mais detalhes na documentação
#>>> os.path.exists('C:\\ o caminho do arquivo')
#>>> os.path.isdir oi isfile para saber se é um outro
#>> os.path.splitext(nome do arquivo) Separa o nome do arquivo e a extensão
# Outros modulos  de servem para trabalhar na lina de comando  é o pathlib, shutil 

# Script para renomear uma grande lista de arquivos

# import os
# os.chdir('c:\\teste')
# print(f'Diretório atual: {os.getcwd()}')
# padrao_nome = input('Qual o padrão de nomes de arquivos a usar(sem a extensão)?')
# for contador, arq in enumerate(os.listdir()):
#     if os.path.isfile(arq):
#         nome_arq, exten_arq = os.path.splitext(arq)
#         nome_arq = psdrao_nome + ' ' + str(contador)

#         nome_novo = f'{nome_arq}{exten_arq}'
#         os.rename(arq, nome_novo)
# print(f'\nArquivos renomeados.')


