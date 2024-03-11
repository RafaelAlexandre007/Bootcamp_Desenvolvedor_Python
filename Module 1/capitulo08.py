##
#MODO DESCRIÇÃO
    #'r' Modo somente leitura (modo padrão).
    #'w' Modo de escrita. Cria um arquivo, caso ainda não exista, ou substitui o arquivo atual.
    #'x' Modo de escrita. Cria um arquivo e, se o arquivo já existir, retorna um erro.
    #'a' Modo de escrita. Cria um arquivo, caso ainda não exista. Se o arquivo já existir, novas escritas serão adicionadas ao final dele.
    #'t' Abre o arquivo no modo texto (modo padrão). 'b' Abre o arquivo no modo binário.
##

# arquivo_valores = open('valores.txt', 'r')
# arquivo_valores.close()
# arquivo_valores = open('valores.txt', 'wb')
# arquivo_valores.close()

# arquivo = open('pasta/cidades.txt', 'r') 
# linhas = arquivo.read() 
# arquivo.close()
# print(linhas)

# arquivo = open('pasta/cidades.txt', 'r') 
# linhas = arquivo.readlines() 
# arquivo.close()
# print(linhas)

# novas_linhas = [] 
# for linha in linhas:
#     novas_linhas.append(linha.rstrip()) 
# print(novas_linhas)
# arquivo.close()

# arquivo = open('pasta/cidades.txt', 'r') 
# for linha in arquivo:
#     print(linha.rstrip()) 
# arquivo.close()

# arquivo = open('pasta/cidades.txt', 'r') 
# soma = 0
# for linha in arquivo:
#     cidade = linha.split(' ')
#     populacao = int(cidade[-1])
#     print(populacao)
#     soma = soma + populacao
# arquivo.close()
# print('Total da soma final: ', soma)

arquivo = open('pasta/cidades.txt', 'a') 
arquivo.write('RJ; São Gonçalo; 1031903\n') 
arquivo.close()

linhas = [
'AL; Maceió; 1005319\n',
'RJ; Duque de Caxias; 878402\n', 'RN; Natal; 862044\n',
'MS; Campo Grande; 843120\n'
]
arquivo = open('pasta/cidades.txt', 'a')
arquivo.writelines(linhas) 
arquivo.close()