#teste 
'''def imprimir(n):
    if ( n==0 ):
        print(n)
    else:
        print(n)
        imprimir(n-1)
n = 100
imprimir(n)'''

#fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

# Exemplo de uso
numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero} é {resultado}')