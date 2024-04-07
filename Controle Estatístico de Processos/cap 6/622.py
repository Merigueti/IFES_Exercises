import matplotlib.pyplot as plt
import math

def desvio_padrao_amostra(tupla):
    n = len(tupla)
    if n < 2:
        return 0.0
    
    media = sum(tupla) / n
    soma_quad_diff = sum((x - media) ** 2 for x in tupla)
    desvio_padrao = math.sqrt(soma_quad_diff / (n - 1))
    
    return desvio_padrao

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


X_ = 210.222/20
s_ = 3.827/20
x_barr = list(map(lambda tup: sum(tup) / len(tup), valores))


n = len(x_barr)
media_x_barra = sum(x_barr) / n

S = [desvio_padrao_amostra(tupla) for tupla in valores]

print(S)

#para grafico do desvio-padrão(s)
LSC_s = 2.568*s_
LM_s = s_
LIC_s = None

#para grafico da média (x_barra)
LSC_x = 10.511+1.954*0.191
LM_x = 10.511
LIC_x = 10.511-1.954*0.191



# Plotar gráfico de controle para amplitudes (R)
plt.figure(figsize=(10, 6))
plt.plot(S, marker='o', linestyle='-', color='b', label='DESVIO PADRÃO (S)')
plt.axhline(y=LSC_s, color='r', linestyle='--', label='LSC')
plt.axhline(y=LM_s, color='g', linestyle='--', label='LM')
if LIC_s is not None:
    plt.axhline(y=LIC_s, color='r', linestyle='--', label='LIC')
plt.title('Gráfico de Controle - DESVIO PADRÃO (S)')
plt.xlabel('Amostra')
plt.ylabel('S')
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