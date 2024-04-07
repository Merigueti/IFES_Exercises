import matplotlib.pyplot as plt

##AMOSTRAS INICIAIS
valores = [(10.69, 10.80, 10.39),
           (10.20, 10.30, 10.72),
           (10.42, 10.61, 10.54),
           (10.98, 10.27, 10.50),
           (10.61, 10.52, 10.67),
           (10.57, 10.46, 10.50),
           (10.44, 10.29, 9.86),
           (10.20, 10.29, 10.41),
           (10.46, 10.76, 10.74),
           (10.11, 10.33, 10.98),
           (10.29, 10.57, 10.65),
           (10.83, 11.00, 10.65),
           (10.35, 10.07, 10.48),
           (10.69, 10.54, 10.61),
           (10.44, 10.44, 10.57),
           (10.63, 9.86, 10.54),
           (10.54, 10.82, 10.48),
           (10.50, 10.61, 10.54),
           (10.29, 10.79, 10.74),
           (10.57, 10.44, 10.52),
           ]

x_barr = list(map(lambda tup: sum(tup) / len(tup), valores))
R = [max(tup) - min(tup) for tup in valores]
total_x_barr = sum(x_barr)
total_R = sum(R)
print(x_barr)
print(R)
print(total_x_barr)
print(total_R)

#Calculo das estatisticas Basicas
X_ = total_x_barr/len(valores)
R_ = total_R/len(valores)

print(X_)
print(R_)

#Cálculo dos Limites de Controle:
#para o grafico da amplitude (R)
D4 = 2.574
LSC_r = 2.574*R_
LM_r = R_
LIC_r = None
#para o graafico da média
LSC_x = X_+1.023*R_
LM_x = X_
LIC_x = X_-1.023*R_

# Plotar gráfico de controle para amplitudes (R)
plt.figure(figsize=(10, 6))
plt.plot(R, marker='o', linestyle='-', color='b', label='Amplitudes (R)')
plt.axhline(y=LSC_r, color='r', linestyle='--', label='LSC')
plt.axhline(y=LM_r, color='g', linestyle='--', label='LM')
if LIC_r is not None:
    plt.axhline(y=LIC_r, color='r', linestyle='--', label='LIC')
plt.title('Gráfico de Controle - Amplitudes (R)')
plt.xlabel('Amostra')
plt.ylabel('R')
plt.legend()
plt.grid(True)
plt.show()

# Plotar gráfico de controle para médias (X)
plt.figure(figsize=(10, 6))
plt.plot(x_barr, marker='o', linestyle='-', color='b', label='Médias (X)')
plt.axhline(y=LSC_x, color='r', linestyle='--', label='LSC')
plt.axhline(y=LM_x, color='g', linestyle='--', label='LM')
plt.axhline(y=LIC_x, color='r', linestyle='--', label='LIC')
plt.title('Gráfico de Controle - Médias (X)')
plt.xlabel('Amostra')
plt.ylabel('X')
plt.legend()
plt.grid(True)
plt.show()