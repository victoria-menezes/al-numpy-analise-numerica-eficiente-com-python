# Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas agora você deve calcular o coeficiente ângular e o linear para a reta da laranja e para a reta da toranja. Use a fórmula de mínimos quadrados para encontrar cada um.
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
fig_citrus = plt.figure(figsize=(7,7), dpi=my_dpi)

ax_citrus = fig_citrus.add_subplot(1,1,1)
ax_citrus.plot(diametro_laranja, peso_laranja)
ax_citrus.plot(diametro_toranja, peso_toranja)
ax_citrus.legend(['Laranja','Toranja'])
ax_citrus.set_xlabel('Diâmetro')
ax_citrus.set_ylabel('Peso')

# y = ax + b
x_l = diametro_laranja
x_t = diametro_toranja

x_li = x_l
y_li = peso_laranja
x_ti = x_t
y_ti = peso_toranja

n_l = np.size(x_li)
n_t = np.size(y_li)

a_l = (n_l*np.sum(x_li*y_li) - np.sum(x_li)*np.sum(y_li)) / (n_l*np.sum(x_li**2) - np.sum(x_li)**2)
a_t = (n_t*np.sum(x_ti*y_ti) - np.sum(x_ti)*np.sum(y_ti)) / (n_t*np.sum(x_ti**2) - np.sum(x_ti)**2)

b_l = np.mean(y_li) - a_l*np.mean(x_li)
b_t = np.mean(y_ti) - a_t*np.mean(x_ti)

y_l = a_l*x_l + b_l
y_t = a_t*x_t + b_t

ax_citrus.plot(x_l, y_l)
ax_citrus.plot(x_t, y_t)

fig_citrus.suptitle(f'Diâmetro x Peso')
fig_citrus.savefig(f'figures/citrus_plot_extra3.png')