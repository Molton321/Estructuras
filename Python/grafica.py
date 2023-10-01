import matplotlib.pyplot as plt

# Representamos el vector
v = [10, 5]
plt.arrow(0, 0, v[0], v[1], head_width=0.1, head_length=0.1)
plt.figure(figsize=(10, 10))

# Representamos la dirección del vector
plt.text(v[0], v[1], "45° al sur del este", rotation=45)

# Mostramos el gráfico
plt.show()