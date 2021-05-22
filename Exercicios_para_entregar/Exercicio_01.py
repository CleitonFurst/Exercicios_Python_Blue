# 01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.


#inserindo dois valores
num1 = int(input('Digete o 1º númeor inteiro :'))
num2 = int(input('Digete o 2º númeor inteiro :'))
#somando os valores 
soma = num1 + num2
#multiplicando os valores
mult = num1 * num2
#divisão dos valores
divint = num1 // num2
#impime os resultasdos
print(f'A soma dos valores é {soma}')
print(f'A multiplicação dos valores é {mult}')
print(f'A divisão inteira entre os dois números é {divint}')
#declaração da variavel maior para comparação
maior = 0
#compara os números para ver qual o maior entre os dois 
if num1 > num2:
    maior = num1
else:
    maior = num2
#impreme o maior número
print(f'O maior valor entre {num1} e {num2} é o {maior}')
#verefica se a soam é par ou impar e imprime o resultado
if soma % 2 == 0:
    print(f'A soma dos valores {num1} e {num2} é Par !!!')
else:
    print(f'A soma dos valores {num1} e {num2} é Impar!!!')
# verefica se a multiplicação entre os números é maior que 40 
if mult >= 40:
    if divint != 0:
        result = mult / divint
    else:
        print(f'O valor do resto da divisão inteira foi igual a ZERO, não é posivel fazer divisão por ZERO!!!!')
    print(f'Resultado do valor {mult} divido por {divint} é igual a {result}')
else:
    print(f'A multiplicação entre dos núumeros {num1} e {num2} não é igual a 40 !!!')
    

    

    