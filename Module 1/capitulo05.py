# Estrutura de Dados
# -> list - Ordenada e mutável
[1, 2, 3, 4]

    #Lista com vaores heterogeneo
[1, 'a', 5.44, True]

    # Lista de valores nulos
['um', 'dois', None, 4]

    #Listas aninhadas
i = [0, 1]
[1, 'dois', i, [2, 3]]

    #Lista vazia
l = []

    #acesso por indice
print(i[0])
    #Acesso por slice
print(i[1:3])

# Lista de 3 idades
idades = [27, 49, 12]
#cria uma lista para armazenar as 10 idade
# idades = [27, 49, 12, 67, 21, 32, 18, 45, 84, 53, 22, 56, 80, 35, 18]
# inicialmente assume que a primeira idade é a maior
maior_idade = idades[0]

# percorre a lista verificando a maior idade
for idade in idades:
    if idade  > maior_idade:
        maior_idade = idade
#exibe a mior idade encontrada
print('Maior idade: ', maior_idade)

#Adiciona valor
idades.append(999)
#Remover
idades.remove(idades[0])
print(idades)

l1 = [30, 10, 20]
l2 = [2, 'a', 5.44, True]

# Operações de concatenação (+), repetição (*) e filiação (in)
print(l1 + l2) 
print(l1 * 3) 
print(10 in l1)
# Funções úteis
print(len(l2)) # len: retorna a quantidade de elementos da lista. print(sum(l1)) # sum: retorna a soma dos elementos de uma lista. print(max(l1)) # max: retorna o maior elemento da lista (!!!!)
# Métodos que alteram os valores internos da lista
l2.reverse() # reverse: inverte a ordem dos elementos
print(l2)
l1.extend([10, 20, 30, 40, 10]) # extend: adiciona elementos de outra sequência print(l1)
l1.sort() # sort: ordena os valores da lista
print(l1)
l2.insert(2, 'novo valor') # insert: adiciona um elemento em um índice especifico print(l2)
l2.pop() # pop: remove o último elemento da lista
print(l2)
l2.clear() # clear: limpa a lista, removendo todos os elementos
print(l2)
# Métodos que retornam valores e não alteram a lista
print(l1.index(40)) # index: retorna o índice da primeira ocorrência do elemento print(l1.count(10)) # count: conta as ocorrências do elemento

# -> tuple - Ordenada e imutável
# -> set - Não ordenada, mutavel e valores unicos
# -> dict - Mapeamento chave e valor, não ordenado e mutavel
