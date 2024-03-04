# define o valor do limiar↵
limiar = 5

menores = [] # cria lista menores
maiores = [] # cria lista maiores
# divide os números de 1 a 10 em maiores e menores
for i in range(10):
    if (i < limiar):
        menores.append(i)
    elif (i > limiar):
        maiores.append(i)
        
# imprime na tela os valores das listas
print('Resultado final')
print('menores:', menores)
print('maiores:', maiores)

#Declaração e Atribuição de Variáveis
nome = 'João' 
var_booleano = True 
raio = 2
pi = 3.14159265359
#atribuição por meio de uma expressão
area = pi * (raio * raio) 
nome_completo = nome + 'da Silva' 
media = (10 + 15 + 20 + 25)/4

print(nome,var_booleano, area)
print(var_booleano)
print(area)
print(nome_completo)
print(media)
 