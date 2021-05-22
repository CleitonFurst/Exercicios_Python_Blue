# 02 - Utilizando estruturas de repetição com variável de controle,
# faça um programa que receba uma string com uma frase informada pelo usuário
# e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela,
# depois mostre na tela essa mesma frase sem nenhuma vogal.

# 05 - Refatore o exercício 2, para que uma função receba a frase,
# faça todo o tratamento necessário e retorne o resultado.
# Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
# cria a função retiravogais
def retiravogais(frase):
    # declara um contador
    cont = 0
    # declara um laço de repetição com variavel de controle
    for i in frase:
        # declara uma condição para fazer a contagem das vogais
        if i in 'AEIOU':
            # adiciona mais 1 ao valor do contador
            cont += 1
    # declaração de um for para fazer a substituição das vogais por vazio
    for i in 'AEIOU':
        # utilizando o replace para substituir o valor da variavel de controle i por vazio
        result = frase.replace(i, '')
        # adiciona a frase sem a vogar contida na variavel de controle
        frase = result
    # declaração de uma lista para guardar os valores de retorno
    result = list()
    # adicionando a frase sem as vogais dentro da lista
    result.append(frase)
    # adicioando o contador dentro da lista
    result.append(cont)
    # retornando a lista
    return result


# inserindo a frase
frase = str(input('Digite uma frase: ').strip().upper())
# atribuindo o valor retonado da função em uma variavel
retorno = retiravogais(frase)
# imprimindo os resultados
print(
    f'Foram retiradas  {retorno[1]} vogais da frase\nEscrita sem as vogais fica -> {retorno[0]}')
