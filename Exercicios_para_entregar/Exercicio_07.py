# 07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
# em uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

#declaração de uma lista composta 
lista = [[],[]]
#declaração do for para inserir 7 valores
for i in range(0,7):
    # adicioanndo valor para num
    num = int(input('Digite um valor :'))
    #comprando se num é par ou impar
    if  num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
#ordenando pares e impares
lista[0].sort()
lista[1].sort()
#imprimindo as pares e os impares separados em ordem crescente
print(f'Os valores pares  digitados {lista[0]} \nOs valores impares digitados {lista[1]}')

