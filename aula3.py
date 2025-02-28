import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

dados = np.loadtxt(url,delimiter=',',usecols=np.arange(1,88,1)) # arange está nos ajudandos a pegar as colunas que queremos, excluindo as colunas de texto. 88 = 7 anos  * 12 meses + 3 (ano incompleto) + 1
dado_transposto = dados.T # transpoe o dado

# datas = dado_transposto[:,0] # todo o intervalo no primeiro (0) array
# com o método acima ele está interpretando as datas (no formato 1.2013) como um número
datas = np.arange(1,88,1) # gerando novamente um array de 1 a 88, para numerar os meses(mes 1, mes 2, mes 20... etc)
precos = dado_transposto[:,1:6]
# formato: [(range de linhas do array), (range de colunas do array)], 1:6 seleciona as colunas 1, 2, 3, 4, e 5

# criando uma variavel para cada coluna de precos, chamando as cidades separadamente
Moscow = precos[:,0] # array unidimensional, uma sequencia de valores
Kaliningrad = precos[:,1]
Petersburg = precos[:,2]
Krasnodar = precos[:,3]
Ekaterinburg = precos[:,4]

Moscow_ano1 = Moscow[0:12] # posicao 0 ate a 11
Moscow_ano2 = Moscow[12:24] # posical 12 ate a 23
Moscow_ano3 = Moscow[24:36] # etc ...
Moscow_ano4 = Moscow[36:48]

Kaliningrad_ano1 = Kaliningrad[0:12] # posicao 0 ate a 11
Kaliningrad_ano2 = Kaliningrad[12:24] # posical 12 ate a 23
Kaliningrad_ano3 = Kaliningrad[24:36] # etc ...
Kaliningrad_ano4 = Kaliningrad[36:48]


# PLOTTING
# MOSCOW
my_dpi = 72
fig_Moscow = plt.figure(figsize=(10,10), dpi=my_dpi)

ax_Moscow = fig_Moscow.add_subplot(1,1,1)
ax_Moscow.plot(np.arange(1,13,1), Moscow_ano1)
ax_Moscow.plot(np.arange(1,13,1), Moscow_ano2)
ax_Moscow.plot(np.arange(1,13,1), Moscow_ano3)
ax_Moscow.plot(np.arange(1,13,1), Moscow_ano4)
ax_Moscow.legend(['ano1','ano2','ano3', 'ano4'])
# np.array_equal(Moscow_ano3, Moscow_ano4) # checa se dois arrays sao iguais
# np.allclose(Moscow_ano3, Moscow_ano4, 0.01) # checa se a diference entre arrays é maior que 0.01

fig_Moscow_crescimento = plt.figure(figsize=(10,10), dpi=my_dpi)
ax_Moscow_crescimento = fig_Moscow_crescimento.add_subplot(1,1,1)
ax_Moscow_crescimento.plot(datas, Moscow)
# queremos fazer uma reta de crescimento do preço das maças (REGRESSÃO LINEAR)
# y = ax + b
x = datas
# y = 0.3*x+80 ?

# calculando o coeficiente angular da reta (o a em y=ax+b):
# (n*soma(xi*yi) - soma(xi)*soma(yi)) / (n*soma(xi^2) - (soma(xi))^2)
# n = número de elementos
yi = Moscow
xi = datas
n = np.size(Moscow)
a = (n*np.sum(xi*yi) - np.sum(xi)*np.sum(yi)) / (n*np.sum(xi**2) - np.sum(xi)**2)
# calculando o coeficiente linear da reta (b):
# (media(yi) - a*media(xi))
b = np.mean(yi) - a*np.mean(xi)

y = a*x + b
# checando a diferença entre a linha que fizemos e o crescimento real: np.sqrt(np.sum(np.power(Moscow-y,2)))
# ou:
print(np.linalg.norm(Moscow-y))
ax_Moscow_crescimento.plot(x,y)

# com a regressão linear conseguimos fazer ESTIMATIVA DE VALORES
# por exemplo:
ax_Moscow_crescimento.plot(41.5, a*41.5+b, '*r') # *r faz ele um ponto vermelho
# estimando valores futuros:
ax_Moscow_crescimento.plot(100, a*100+b, '*r') # *r faz ele um ponto vermelho

# KALININGRAD
nan_location = np.asarray(np.isnan(Kaliningrad)).nonzero()[0] # acha as localizacoes dos nans 
for nan_pos in nan_location:
    Kaliningrad[nan_pos] = np.mean(Kaliningrad[nan_pos-1]+Kaliningrad[nan_pos+1])

fig_Kaliningrad = plt.figure(figsize=(10,10), dpi=my_dpi)

ax_Kaliningrad = fig_Kaliningrad.add_subplot(1,1,1)
ax_Kaliningrad.plot(np.arange(1,13,1), Kaliningrad_ano1)
ax_Kaliningrad.plot(np.arange(1,13,1), Kaliningrad_ano2)
ax_Kaliningrad.plot(np.arange(1,13,1), Kaliningrad_ano3)
ax_Kaliningrad.plot(np.arange(1,13,1), Kaliningrad_ano4)
ax_Kaliningrad.legend(['ano1','ano2','ano3', 'ano4'])


def save_fig(my_fig, my_ax, cidade : str = ''):
    my_ax.set_xlabel('Mês')
    my_ax.set_ylabel('Preço')
    my_fig.suptitle(f'Preço {cidade}')
    my_fig.savefig(f'{cidade}_plot.png')

save_fig(fig_Moscow, ax_Moscow, 'figures/Moscow')
save_fig(fig_Moscow_crescimento, ax_Moscow_crescimento, 'figures/Moscow_crescimento')
save_fig(fig_Kaliningrad, ax_Kaliningrad, 'figures/Kaliningrad')
