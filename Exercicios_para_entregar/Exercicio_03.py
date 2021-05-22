# 03 - Utilizando estruturas de repetição com teste lógico,
# faça um programa que peça uma senha para iniciar seu processamento, 
# só deixe o usuário continuar se a senha estiver correta, 
# após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
# onde o computador vai “pensar” em um número entre 0 e 10.
# O jogador vai tentar adivinhar qual número foi escolhido até acertar, 
# a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
# no final mostre quantos palpites foram necessários para vencer.


usuario = str(input('Digite o nome de usúario :').strip().upper())
senha = str(input('Digite a senha :'))
while True:
    verefica_u =str(input('Usuario:').strip().upper())
    verefica_s = str(input('Senha:').strip().upper())
    if verefica_u == usuario and verefica_s == senha :
        break
    else:
        print('Usuario ou senha incorretos !!!!\nTente novamente!!!')
print('Seja muito bem vindo !!!')
print('vamos jogar um jogo de adivinhação')
num = int(input('escolah um número entre 0 e 10 que você acha que o computador sorteou : '))
   