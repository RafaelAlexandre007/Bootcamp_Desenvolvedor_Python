# Para Google colab
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
l2 = [2, 'a', 5.44, True] 
#Erro print(max(l2))
idades = [27, 49, 12, 67, 21, 32, 18, 45, 84, 53, 22, 56, 80, 35, 18] 
print('Maior idade:', max(idades))

# -> tuple - Ordenada e imutável
tupla = (0, 1, 2, 3, 4) 
print(tupla)
# Tupla heterogênea
tupla2 = (2, 'a', 5.44, True, None) 
print(tupla2)
# Tupla vazia
tupla3 = () 
print(tupla3)
# acesso por índices
print(tupla[0]) 
print(tupla[3]) 
print(tupla[-1])
# acesso por slices
print(tupla2[1:4]) 
print(tupla2[-2:]) 
print(tupla2[:])

t1 = (30, 10, 20)
t2 = (2, 'a', 5.44, True)
# Operações de concatenação (+), repetição (*) e filiação (in)
print(t1 + t2) 
print(t1 * 3) 
print(10 in t1)
# Funções úteis
print(len(t2)) # len: retorna a quantidade de elementos da tupla 
print(min(t1)) # min: retorna o menor elemento da tupla 
print(max(t1)) # max: retorna o maior elemento da tupla 
print(sum(t1)) # sum: retorna a soma dos elementos da tupla
# Métodos que retornam valores
print(t1.index(20)) # index: retorna o índice da primeira ocorrência do elemento 
print(t2.count('a')) # count: conta as ocorrências do elemento

t1 = (1, 2, 3) 
#Erro t1[0] = 4

# -> set - Não ordenada, mutavel e valores unicos
c1 ={3, 0, 1, 2, 4, 3, 3, 3, 3}
print(c1)

    ## OperaçAo com conjuntos
c2 = { 2, "a", 5.44, True}
print(c2)


# Criação dos conjuntos A e B
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 
print('A:', A) 
print('B:', B)
# Operação de União: (A ∪ B) 
print('A | B =>', A | B) 
print('A.union(B) =>', A.union(B))
# Operação de Interseção: (A ∩ B)
print('A & B =>', A & B) 
print('A.intersection(B) =>', A.intersection(B))
# Operação de Diferença: (A - B) e (B - A)
print('A - B =>', A - B) 
print('A.difference(B) =>', A.difference(B)) 
print('B - A =>', B - A) 
print('B.difference(A) =>', B.difference(A))                

#Criação dos conjuntos A e B
c1 = {1, 2, 3, 4, 5} 
c2 = {4, 5}
c3 = {91, 92, 93}
# Adiciona um elemento ao conjunto
c1.add(6) 
print(c1)
# Adiciona os elementos de uma sequência iterável
c1.update([2, 4, 6, 8]) 
print(c1)
# Descarta um elemento do conjunto,
c1.discard(8)
print(c1)
# Diferentemente do set.remove(), o discard não gera um erro # se o elmento a ser removido não existir
c1.discard(99)
print(c1)
# Verifica se os conjuntos são disjuntos, ou seja, # se não possuem nenhum elemento em comum 
print(c1.isdisjoint(c2))
print(c1.isdisjoint(c3))
# Verifica se o conjunto é subconjunto de outro
print(c1.issubset(c2)) 
print(c2.issubset(c1))
# Verifica se o conjunto contém outro conjunto (superset)
print(c1.issuperset(c2)) 
print(c2.issuperset(c1))

# Criação das listas de alunos das turmas
ING = ['Gabriel', 'Caio', 'Maria', 'Ana', 'Juliano', 'Flávia', 'Rubens', 'Bruna'] 
ESP = ['Caio', 'Artur', 'Beatriz', 'Carolina', 'Maria', 'Juliano', 'Bruna', 'Rui'] 
FRA = ['Pedro', 'Bruna', 'Paula', 'Tiago', 'Maria', 'Flávia', 'Rui', 'Carolina']
# Concatenação de todas as listas de alunos
ALL = ING | ESP | FRA

# Exibição do resultado
print('Relação de todos os alunos da escola:') 
print(ALL)

# 1 – Interseção entre os pares de turmas: (ING & ESP), (ING & FRA) e (ESP & FRA) 
# 2 – Calcula a união das interseções
ALUNOS_DESCONTO = (ING & ESP) | (ING & FRA) | (ESP & FRA)
# Exibição do resultado
print('Relação de dos alunos com desconto:') 
print(ALUNOS_DESCONTO)

# 1 – Interseção entre os pares de turmas: (ING & ESP), (ING & FRA) e (ESP & FRA) 
# 2 – Calcula a união das interseções
ALUNOS_DESCONTO = (ING & ESP) | (ING & FRA) | (ESP & FRA)
# Exibição do resultado
print('Relação de dos alunos com desconto:') 
print(ALUNOS_DESCONTO)

# -> dict - Mapeamento chave e valor, não ordenado e mutavel
 #Dicionário onde as chaves são do tipo string
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'} 
print(d1)
# Dicionário onde as chaves são do tipo inteiro
d2 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'} 
print(d2)
# Dicionário com chaves de tipos mistos
d3 = {2: 'a', 5.44: True, 'key': None} 
print(d3)
# Dicionário vazio
d4 = {} 
print(d4)

# Criação dos dicionários
d1 = {2: 'dois', 1: 'um', 4: 'quatro', 3: 'três', 0: 'zero'}
d2 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
# Acesso aos elementos
print(d1[0]) 
print(d1[2])
print(f'Meu nome é {d2["nome"]} e tenho {d2["idade"]} anos')

# Criação do dicionário
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
# Acesso por meio do operador []
print(d1['endereço'])

# Criação do dicionário
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'}
# Acesso por meio do método get()
print(d1.get('endereço'))

# Criação do dicionário
d1 = {'nome': 'Antônio', 'idade': 36, 'sexo': 'masculino'} 
print(d1)
# Atualização do valor da chave 'nome'
d1['nome'] = 'Antônio Carlos'
print(d1)
# Adição da chave 'endereço'
d1['endereço'] = 'Rua 123'
print(d1)

# Cria o dicionário
d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4} 
print(d1)
# Encontra a maior e menor chave
print('Maior e menor chave:', max(d1), min(d1))
# Adiciona elementos de um outro dicionario
d1.update({'cinco': 5, 'seis': 6}) 

print(d1)
# Verifica se o dicionário possui as seguintes chaves
print("A chave 'dois' está no dicionário?", 'dois' in d1) 
print("A chave 'cinco' não está no dicionário?", 'dois' in d1)
# Remove o elemento com chave 'zero'
d1.pop('zero') 
print(d1)

# Cria o dicionário
d1 = {'zero': 0, 'um': 1, 'dois': 2, 'três': 3, 'quatro': 4}
# Itera sobre as chaves
for key in d1:
    if key == 'três':
        print('Chave três encontrada!')

for key in d1.keys(): 
    if key == 'dez':
        print('Chave quatro encontrada!')

# Itera sobre os valores
soma = 0
for value in d1.values():
    soma = soma + value
print('Soma dos valores do dicionário:', soma)

# Itera sobre os itens
for key, value in d1.items(): 
    print(key, value)

