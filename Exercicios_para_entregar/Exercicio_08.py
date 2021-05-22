# 08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também
# o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai
# se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import datetime
# declarando o dicionario
dados = dict()
# criando as chaves e inserindo os valores
dados['nome'] = str(input('Digite o nome :'))
dados['anonac'] = int(input('Digite o ano de nacimento :'))
dados['carteira'] = int(input('Digite  o número da carteira de trabalho :'))
# condicional que verefica se o númeor da carteira de trabalho incerrida e maior que zero
if dados.get('carteira') != 0:
    # adiciona os dados do ultimo emprego
    dados['anocont'] = int(input('Digite  o ano de contratação :'))
    dados['salario'] = float(input('Digite o salário :'))
# função datetime que pega o ano atual
ano = datetime.now()
# faz o calculo do ano atual menos o ano que começou a trablahar para ver quantos anos de trbalho tem
dados['idade'] = int(ano.year) - dados.get('anonac')
# condicional que verefica se o número da carteira de trabalho é diferente de zero
if dados.get('carteira') == 0:
    # imprimindo os dados sem os dados do trabalho
    print(
        f'Se o(a) {dados["nome"]} começar a trabalhar este ano ainda vai levar 35 anos, ai vai se apposentar com {dados["idade"] + 35} anos')
else:
    # imprimindo o resultado completo caso tenha todos os dados
    trabalhados = int(ano.year) - dados.get('anocont')
    print(trabalhados)
    print(f'Como o(a) {dados["nome"]} começou a trabalhar no ano de {dados["anocont"]}'
          ' e atualamente tem {dados["idade"]} vai se aposentar com {dados["idade"] + 35 - trabalhados} anos de idade com 35 anos de contribuição')
