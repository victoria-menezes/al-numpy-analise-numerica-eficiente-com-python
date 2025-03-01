# Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Continuando com o projeto das laranjas/toranjas, agora você deve calcular o coeficiente angular utilizando a geração de números aleatórios. Assuma que já conhece b e que este é igual a 17.

import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,6,1),skiprows=1)

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

b_l = b_t = 17

ax_citrus.set_yticks(np.arange(0,276,25))

np.random.seed(9)
a_candidates = np.random.uniform(low=8.0, high=20.0, size=400)

norma_l = np.array([])
norma_t = np.array([])

for i in range(100):
    norma_l = np.append(norma_l, np.linalg.norm(peso_laranja-(a_candidates[i]*x_l+b_l)))
    norma_t = np.append(norma_t, np.linalg.norm(peso_toranja-(a_candidates[i]*x_t+b_t)))

a_l = a_candidates[np.where(norma_l == min(norma_l))[0]]
a_t = a_candidates[np.where(norma_t == min(norma_t))[0]]

y_l = a_l*x_l + b_l
y_t = a_t*x_t + b_t

ax_citrus.plot(x_l, y_l)
ax_citrus.plot(x_t, y_t)


fig_citrus.suptitle(f'Diâmetro x Peso')
fig_citrus.savefig(f'figures/citrus_plot_extra4.png')