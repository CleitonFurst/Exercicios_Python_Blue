# 04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional:
# valide a data e retorne 'data inválida' caso a data seja inválida.


def verefica_mes(data):
    ''' Função para fazer a verificação se a data é valida ou não '''
    mes = int(data[3:5])#pega somente o mês da string e converte em int para comparação 
    ano = int(data[6:])#pega somente o ano da string  e converte em int para comparação 
    dia = int(data[:2])#pega somente o dia da string e converte em int para comparação 
    #compara se o mês digitado esta entre os meses uqe terminam com o dia 31
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia <= 31:
           return True
        else: 
            return False
    
    #compara se o mês digitado esta entre os meses uqe terminam com o dia 30
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia <= 30:
            return True 
        else:
            return False   
    elif mes == 2:
        # Testa se é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia <= 29:
                return True            
            elif dia <= 28:
                    return True
            else:
                return False
    else:
         return False


def data_descricao(data):
    verefica = verefica_mes(data)
    #verefica se o retorno da função verefica_mes é verdadeira ou falsa 
    if verefica == True:
        lista_de_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes = int(data[3:5])
        mes_desc = lista_de_mes[mes -1]
        return mes_desc
    else:
        print(f'A data não é valida !!!')

data = input('Digite uma data no formato DD/MM/AAAA :')
mes = str(data_descricao(data))
ano = int(data[6:])
dia = int(data[:2])
print(f'{dia} de {mes} de {ano}')