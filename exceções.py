# Execeção é um objeto que representa um erro que ocorreu ao excutar po progrma
# usa-se o bloco try .... except

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro numer: '))
# try:
#     r = round(n1 / n2, 2)
# except ZeroDivisionError:
#     print(f'Não é possivel divifdir por zero')
# else: 
#     print(f'Resultado: {r}')

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True: # while é para a função so para seguir os dados forem informar correto
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro numer: '))
            break
        except ValueError:
            print(f'ocorreu um erro ao ler o valor. Tente novamente.')
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possivel divifdir por zero')
    except:
        print(f'Ocorreu uma erro desconhecido')
    else: 
        print(f'Resultado: {r}')
    finally:
        print(f'\nFim do calculo')




    



