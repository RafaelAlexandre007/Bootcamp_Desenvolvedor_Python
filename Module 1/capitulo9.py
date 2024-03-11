potencias = []
for item in range(1, 11):
    potencias.append(item ** 2) 
print(potencias)


print( [n * 10 for n in range(1, 16)] ) # Multiplica por 10 os números de 1 a 15 
print( [c.upper() for c in 'antonio'] ) # Cria lista com os caracteres em maísculo 
print( [(n % 2 == 0) for n in range(0, 10)] ) # Indica se n é par ou não

potencias = []
for item in range(1, 11):
    if item % 2 != 0: potencias.append(item ** 2)
print(potencias)

# todos os números elevado à potência 2
dict_todos = {}
for item in range(1, 11):
    dict_todos[item] = item ** 2 
print('Todos numeros:', dict_todos)
# apenas números ímpares elevado à potência 2
dict_impares = {}
for item in range(1, 11):
    if item % 2 != 0: dict_impares[item] = item ** 2
print('Números ímpares:', dict_impares)

# todos os números elevado à potência 2
dict_todos = {item: item ** 2 for item in range(1, 11)} 
print('Todos numeros:', dict_todos)
# apenas números ímpares elevado à potência 2
dict_impares = {item: item ** 2 for item in range(1, 11) if item % 2 != 0} 
print('Números ímpares:', dict_impares)

# Função que calcula o triplo de número
triplo = lambda x: x * 3
# Calcula o triplo dos números de uma lista
lista = [4, 5, 9, 7, 0, 1, 8] 
print(list(map(triplo, lista)))

print(list(map(lambda x: x * 3, [4, 5, 9, 7, 0, 1, 8])))

nome = 'antonio' 
if len(nome) > 5:
    var = 100 
else:
    var = 0
print('O valor de var é:', var)

nome = 'antonio'
var = 100 if len(nome) > 5 else 0 
print('O valor de var é:', var)