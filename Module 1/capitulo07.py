import areas

import areas as ar
print(areas.quadrado(2))

print(ar.circulo(2,2))

# modulo com funções matemáticas para cálculos mais complexos
import math
print('Função cosseno:', math.cos(100)) 
print('Função log:', math.log(10))

# modulo para construção de sequências elaboradas
import itertools
print(list(itertools.combinations('RAFAEL', 3))) # combinação de 3 em 3 
print(list(itertools.permutations(['a', 'b', 'c'], 2))) # permutação de 2 em 2

# modulo para manipulação de timestamps (datas, horários, deltas etc.)
from datetime import datetime, timedelta
print('Datetime atual:', datetime.now())
print('Datetime após 7 dias:', datetime.now() + timedelta(days=7))

# modulo para criação de números e sequências randômicas
import random
print('Numero aleatório entre 0 e 1:', random.random()) 
print('Inteiro aleatório entre 50 e 100:', random.randint(50, 100))

# modulo para funcionalidades que dependem do sistema operacional
import os
#os.mkdir('pasta') # cria um diretório chamado pasta
#print('Caminho completo:', os.path.join('/', 'pasta', 'arquivo.txt'))

# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# Repositório oficial de pacotes Python: https://pypi.org/
# Página oficial do pacote pandas: https://pandas.pydata.org/
# Tutorial de instalação pip: https://pip.pypa.io/en/stable/installation/