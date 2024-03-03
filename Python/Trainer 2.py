#conversor de temperatura Celsius para Farenhit
'''temp1 = float(input('Insira a temperatura em Graus Celsius: '))

convs = (temp1 * 9/5) + 32

print('Sua temperatura em Farenhit é: ',convs,'°F')'''

#Aluguel de carro
dias = float(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos Kms o carro percorreu?: '))
env = dias * 60
din = km * 0.15
fyt = env + din
print('O preço do aluguel do carro é de R${}'.format(fyt))
