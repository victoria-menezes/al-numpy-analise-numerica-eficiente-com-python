import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,6,1),skiprows=1)
print(dados)