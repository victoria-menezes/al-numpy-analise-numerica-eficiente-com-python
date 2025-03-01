# Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora você deve selecionar parte dos dados. As colunas que iremos avaliar são as de diâmetro e peso. Crie arrays específicos para guardar o diâmetro e peso da laranja e toranja. O diâmetro está na coluna zero e o peso na coluna 1. Os dados referentes a laranja vão até a linha 4999 e os referentes à toranja iniciam na linha 5000 do arquivo.

# Após fazer a seleção de dados, importe a biblioteca matplotlib e crie um gráfico para a laranja e para a toranja do peso pelo diâmetro.
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,6,1),skiprows=1)
print(np.shape(dados))


diametro_laranja = dados[:5000,0]
peso_laranja = dados[:5000,1]
diametro_toranja = dados[5000:,0]
peso_toranja = dados[5000:,1]

my_dpi = 72
fig_citrus = plt.figure(figsize=(5,5), dpi=my_dpi)

ax_citrus = fig_citrus.add_subplot(1,1,1)
ax_citrus.plot(diametro_laranja, peso_laranja)
ax_citrus.plot(diametro_toranja, peso_toranja)
ax_citrus.legend(['Laranja','Toranja'])

ax_citrus.set_xlabel('Diâmetro')
ax_citrus.set_ylabel('Peso')
fig_citrus.suptitle(f'Diâmetro x Peso')
fig_citrus.savefig(f'figures/citrus_plot_extra2.png')