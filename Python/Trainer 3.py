#exemplo 1
'''num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

ini = min(num1, num2)
fim = max(num1, num2)

for i in range (ini , fim + 1):
  print(i)'''

#exemplo2
'''numero = int(input('Digite um numero: '))

if numero < 0:
  print("apenas maior que zero")

else:
  fatorial = 1

  for i in range (1, numero + 1):
    fatorial *= i
    print(fatorial)'''

#exemplo3
'''soma = 0
for i in range (1,50):
  soma += i
  print(soma)'''

#exemplo4
'''numero = int(input('Digite um numero: '))

if (numero%2)==0:
  print("é par")
else:
  print("é impar")'''

#exmplo5
'''num = 10
while num <= 200:
    if num % 2 != 0:
        print(num)
    num += 1'''

#exemplo6
'''nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Seu nome é {}, Você possui {} anos e é maior de idade".format(nome,idade))
else:
    print("Seu nome é {}, Você possui {} anos e não é maior de idade".format(nome,idade))'''

'''#exemplo7
a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))

if a >= b and a >= c:
    maior = a 
elif b >= a and b >=c:
    maior = b
else:
    maior = c
print("o maior numero é {}".format(maior))'''

#exemplo8

''' a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
c = int(input("digite o terceiro numero: "))

ordm = max(a,b,c)

if a >= b and a >= c:
    maior = a 
elif b >= a and b >=c:
    maior = b
else:
    maior = c
print("o maior numero é {}".format(maior))
print("Os números em ordem crescente são:", *sorted([a, b, c]))'''