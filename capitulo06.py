# define as listas com os números a serem somados
l1 = [1, 2, 3, 4, 5]
l2 = [3, 1, 5, 9, 0, 8, 2, 3, 4] 
l3 = [12, 43, 23, 12, 789]
# itera sobre cada lista e soma seus elementos
soma_l1 = 0 
for item in l1:
    soma_l1 = soma_l1 + item
soma_l2 = 0 
for item in l2:
    soma_l2 = soma_l2 + item
soma_l3 = 0 
for item in l3:
    soma_l3 = soma_l3 + item
# exibe os resultados
print(f'Resultado: l1={soma_l1}, l2={soma_l2}, l3={soma_l3}')

# define as listas com os números a serem somados
l1 = [1, 2, 3, 4, 5]
l2 = [3, 1, 5, 9, 0, 8, 2, 3, 4] 
l3 = [12, 43, 23, 12, 789]
# declaraca a função que soma os elementos da lista
def soma_lista(lista): 
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

# chama a função para cada lista
soma_l1 = soma_lista(l1) 
soma_l2 = soma_lista(l2) 
soma_l3 = soma_lista(l3)
print(f'Resultado: l1={soma_l1}, l2={soma_l2}, l3={soma_l3}')

# exibe mensagem de boas vindas à uma pessoa
def boas_vindas(nome):
    print(f'Olá {nome}. Seja bem-vindo (a)!')
# calcula a área de um quadrado: l x l
def area_quadrado(lado): 
    return lado * lado
# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura): 
    return (base * altura)/2
# Realiza as chamadas das funções
boas_vindas('Priscila') 
print(area_triangulo(4, 5))
boas_vindas('Maria') 
boas_vindas('Joana')
print(area_quadrado(4)) 
print(area_quadrado(10))
boas_vindas('Antônio') 
print(area_quadrado(10))
print(area_triangulo(5, 2))
print(area_triangulo(4, 5))

# Realiza uma divisão. Se o divisor é zero, retorna uma mensagem de erro.
def div(dividendo, divisor): 
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return
    return dividendo / divisor
# Função similar à função div, mas que retorna o dividendo e o resto da divisão.
def div_qr(dividendo, divisor): 
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return
    quociente = dividendo // divisor 
    resto = dividendo % divisor 
    return (quociente, resto)
print('div(10, 4) ==>', div(10, 4)) # dividento=10 e divisor=4 
print('div_qr(10, 4) ==>', div_qr(10, 4)) # dividento=10 e divisor=4 
print('div(10, 0) ==>', div(10, 0)) # dividento=10 e divisor=0

# atribuição dos múltiplos valores em uma variável única do tipo tupla
resultado = div_qr(21, 5)
print('resultado:', resultado, type(resultado))
# atribuição dos múltiplos valores em variáveis separadas
quociente, resto = div_qr(21, 5) 
print('quociente:', quociente, type(quociente)) 
print('resto:', resto, type(resto))

# Verifica se é um divisor inválido (divisor == 0)
def divisor_invalido(divisor): 
    if divisor == 0:
        print('ERRO: Divisor igual à zero!')
        return True 
    return False
# Retorna o resultado de uma divisão
def div(dividendo, divisor):
    if divisor_invalido(divisor):
        return
    return dividendo / divisor
# Retorna o quociente e o resto de uma divisão
def div_qr(dividendo, divisor): 
    if divisor_invalido(divisor):
        return
    quociente = dividendo // divisor 
    resto = dividendo % divisor 
    return (quociente, resto)

# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura): 
    return (base * altura)/2
print(area_triangulo(5, 10))

# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura): 
    return (base * altura)/2
print(area_triangulo(altura=10, base=5))

# calcula a área de um triângulo: (b x h) / 2
def area_triangulo(base, altura): 
    return (base * altura)/2
print(area_triangulo(5))

def exibe_pessoa(nome, idade=30):
    print(f'Meu nome é {nome} e tenho {idade} anos.')
exibe_pessoa('Antônio') 
exibe_pessoa('Antônio', 36)