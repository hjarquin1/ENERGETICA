import matplotlib.pyplot as plt

# Preguntamos por el year inicial 

inicio = int(input("\nIntroduce el año inicial: "))

# preguntal el year final 

final = int(input("\nIntroduce el año final: "))

# definir un diccionario vacio para guardar las ventas de cada año
ventas = {}

# Bucle iteratrivo para pregunar las ventas de cada año

for i in range(inicio, final+1):
    ventas[i] = float(input("\nIntroduce las ventas de año "+ str(i)+": " ))

# Definir figura para matplot 

fig, ax = plt.subplots()

# Dibujar la linea 

ax.plot(ventas.keys(), ventas.values())

# Mostrar el grafico 

plt.show()