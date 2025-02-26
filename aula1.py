import numpy as np

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) # arange está nos ajudandos a pegar as colunas que queremos, excluindo as colunas de texto. 88 = 7 anos  * 12 meses + 3 (ano incompleto) + 1

print(dados)
print()

print (dados.ndim) # retorna a dimensao do nosso dado, nesse caso, 2 dimensões
print (dados.size) # retorna a quantidade de items em nosso dado
print (dados.shape) # retorna as dimensões do nosso dado

dado_transposto = dados.T
print (dado_transposto) # transpoe o dado

