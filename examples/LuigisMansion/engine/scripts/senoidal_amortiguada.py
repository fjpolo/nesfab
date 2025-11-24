import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la onda coseno amortiguada con 1.5 periodos, amortiguación 0.5 y 30 puntos
amplitud = 1.0
periodos = 1.5
amortiguamiento = 0.5
puntos_por_periodo = 20  # Se establece la cantidad de puntos a 30 / 1.5 periodos

# Crear una LUT con valores de una onda coseno amortiguada
x = np.linspace(0, periodos, int(periodos * puntos_por_periodo))
y = amplitud * np.exp(-amortiguamiento * x) * np.cos(2 * np.pi * periodos * x)

# Normalizar la LUT al rango de 0.0 a 1.0
y_normalized = (y - np.min(y)) / (np.max(y) - np.min(y))

print(x / 2.0)
print(y_normalized)

# Visualizar la LUT
plt.plot(x, y_normalized)
plt.title('Onda Coseno Amortiguada (1.5 periodos, amortiguación 0.5, 30 puntos)')
plt.xlabel('Entrada (0.0 - 1.5)')
plt.ylabel('Salida Normalizada (0.0 - 1.0)')
plt.grid(True)
plt.show()
