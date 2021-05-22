# 03 - Utilizando estruturas de repetição com teste lógico,
# faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, 
# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
# onde o computador vai “pensar” em um número entre 0 e 10.
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
# no final mostre quantos palpites foram necessários para vencer.

from random import randint
print('Crie um usuario e uma senha\n')
#realiza um cadastro do usuario
usuario = str(input('Digite o usuario:').strip().upper())
senha = str(input('Digite a senha:'))
#declaração do laço de repetição que vai fazer a validação do login
while True:
    print('Fazer login ....\n')
    verefica_u =str(input('Usuario:').strip().upper())
    verefica_s = str(input('Senha:').strip().upper())
    #verefica se o usuario e senha digitados estão corretos
    if verefica_u == usuario and verefica_s == senha :
        break
    else:
        print('Usuario ou senha incorretos  !!!!\nTente novamente!!!')
print('Bem vindo ao jogo !!!')
print('Vamos jogar um jogo de adivinhação !!!')
#gera um núero aleatório de 0 a 10 
comput = randint(0 , 10)
#variavel que conta quantos palpites foram necessários
cont = 0
#declaração do laço de repetição para vereficar se o usuario acertou o número sorteado
while True:
    cont += 1
    num = int(input('Escolha um número de 0 a 10 que você acha que o computador escolheu  : '))
    #validação se o número digitado for menor que o sorteado
    if num < comput :
        print('O número é menor do que o sorteado!!!')
        #validação se o número digitado for maior que o sorteado
    elif num > comput :
        print('O número é maior do que o sorteado !!!')
    #se nenhuma condição for atendida o usuario acertou 
    else:
        print('Parabéns você acertou ')
        break
print(f'Foram precisos {cont} palpites para acertar !!!')

   