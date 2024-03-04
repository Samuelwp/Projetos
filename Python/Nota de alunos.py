nome = str(input('Digite seu nome:'))
print('Seja bem vindo! {}'.format(nome))

n1 = float(input('Digite nota 1: '))
n2 = float(input('Digite nota 2: '))
n3 = float(input('Digite nota 3: '))
n4 = float(input('Digite nota 4: '))

med = ( n1 + n2 + n3 + n4 ) / 4
print('Sua media é {}'.format(med))

if med >= 7:
    print('Você está aprovado, parabens!')
    
if med > 4 and med <6.9:
    print('você esta de prova final')  

elif med < 4:
    print('você esta reprovado')


