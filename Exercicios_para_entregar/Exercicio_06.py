# 06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

#declaração de uma lista com as perguntas
perguntas = ['Telefonou para a vítima?',
             'Esteve no local do crime?',
             'Mora perto da vítima?',
             'Devia para a vítima?',
             'Já trabalhou com a vítima?']
# declarando o contador
cont = 0
#declarando o laço de repetição for para percorrer a litas de perguntas
for i in perguntas: 
    #perguntando ao usuario utilizando strip, upper e [0] para filtras a string digitada e garantir que retorne apenas S ou N
    resposta = str(input(f'{i} (S/N):').strip().upper()[0])
    #validando a condição se for S
    if resposta == 'S':
        #contando quantas respostas foram S
        cont += 1
    else:
        #para apenas continuar o programa
        continue
#condicionais para vereficar quantas respostas foram sim e imprimier o resultado de cada caso
if cont == 2:
    print('2 respostas foram sim pessoa considerada Suspeita !!!')
elif cont == 3 or cont == 4:
    print(f'{cont} resposatas sim pessoa considerada Cúmplice !!!')    
elif cont == 5:
    print('5 Respostas sim pessoa considerada Assassina> Você esta preso!!!!')
else:
    print('Pessoa inocente !!!')