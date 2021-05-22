# 02 - Utilizando estruturas de repetição com variável de controle,
# faça um programa que receba uma string com uma frase informada pelo usuário
# e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela,
# depois mostre na tela essa mesma frase sem nenhuma vogal.

#insere a frase 
frase = str(input('Digite uma frase :').upper())
#declaro um contador para contar quantas vogais tem na frase 
cont = 0
#declaração do for para percorer todas as letras da minha frase
for i  in frase:
    #condição para contar apenas a vogais da frase
    if i in 'AEIOU':
        #aoma mais 1 ao valor de cont
        cont += 1
#declaração do for para retirar as vogais
for i in 'AEIOU':
    #adicionando 
    cons = frase.replace(i,'')
    frase = cons
print(f'As vogais (a,e,i,o,u) aparecem na frase {cont} e a frase sem as vogais fica {cons}')