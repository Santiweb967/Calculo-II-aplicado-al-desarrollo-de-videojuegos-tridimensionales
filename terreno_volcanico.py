import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Crear una malla de puntos (x, y)
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

# Paso 2: Definir la función del terreno (volcán)
Z = np.exp(-0.1 * (X**2 + Y**2)) * (np.sin(2 * X) + np.cos(2 * Y))

# Paso 3: Graficar superficie 3D
fig1 = plt.figure(figsize=(10, 6))
ax1 = fig1.add_subplot(111, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='hot', edgecolor='none')
ax1.set_title('Terreno Volcánico (Superficie 3D)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

# Paso 4: Graficar curvas de nivel
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.contour(X, Y, Z, levels=30, cmap='hot')
ax2.set_title('Curvas de Nivel del Terreno')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

# Paso 5: Calcular y graficar campo de gradiente
dx, dy = np.gradient(Z, x[1] - x[0], y[1] - y[0])
fig3, ax3 = plt.subplots(figsize=(8, 6))
ax3.quiver(X, Y, dx, dy)
ax3.set_title('Campo de Gradiente del Terreno')
ax3.set_xlabel('x')
ax3.set_ylabel('y')

plt.tight_layout()
plt.show()
