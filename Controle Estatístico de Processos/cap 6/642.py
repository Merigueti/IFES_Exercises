import matplotlib.pyplot as plt

valores = [22.7,
           20.7,
           21.2,
           19.7,
           18.7,
           24.2,
           26.8,
           18.9,
           24.5,
           24.9,
           19.2,
           16.8,
           23.0,
           19.8,
           18.8,
           19.1,
           22.6,
           20.9,
           17.4,
           25.6,
           22.0,
           21.8,
           23.2,
           23.5,
           26.0,]

rm = [abs(valores[i] - valores[i+1]) for i in range(len(valores) - 1)]
x_barr = [(valores[i] + valores[i+1])/2 for i in range(len(valores) - 1)]

print(x_barr)

X_ = sum(valores)/len(valores)
Rm = sum(rm)/len(rm)


#para grafico de Rm
LSC_rm = 3.267*2.95
LM_rm = Rm
LIC_rm = None

#para grafico x
LSC_x = 21.57+1.880*2.95
LM_x = 21.57
LIC_x = 21.57-1.880*2.95



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