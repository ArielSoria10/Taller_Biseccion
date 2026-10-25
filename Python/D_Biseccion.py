import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. FUNCIÓN DE BISECCIÓN (Algoritmo 2.1 con Validaciones: Ariel Soria)
# =============================================================================
def biseccion(f, a, b, TOL, N0):
   
    if not isinstance(N0, int) or N0 <= 0:
        raise ValueError("El número máximo de iteraciones (N0) debe ser un entero positivo.")
    
    # 2. Validar que exista cambio de signo en el intervalo [a, b]
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos a y b (f(a) * f(b) < 0).")
    
    # -------------------------------------------------------------
    # IMPLEMENTACIÓN DEL ALGORITMO 2.1
    # -------------------------------------------------------------
    # Paso 1: Tome i = 1 y FA = f(a)
    i = 1
    FA = f(a)
    
    while i <= N0:
        p = a + (b - a) / 2.0
        FP = f(p)
        
        if FP == 0 or (b - a) / 2.0 < TOL:
            return p
        
        i += 1
        
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones.")
# =============================================================================
# 2. CÁLCULO DE LA SOLUCIÓN
# =============================================================================
# Definición de la función f(x) = x - tan(x)
f = lambda x: x - np.tan(x)

# Ejecución de la bisección en el intervalo [4, 4.5] con TOL = 1e-5
x_sol = biseccion(f, a=4.0, b=4.5, TOL=1e-5, N0=100)
print(f"Solución encontrada: x ≈ {x_sol:.6f}")


# =============================================================================
# 3. GENERACIÓN DE LA GRÁFICA
# =============================================================================
# Dominio de x en [0, 5]
x = np.linspace(0, 5, 2000)

y_x = x
y_tan = np.tan(x)

# Filtrar puntos cerca de las asíntotas para evitar líneas de conexión verticales
threshold = 20
y_tan[np.abs(y_tan) > threshold] = np.nan

plt.figure(figsize=(10, 6), dpi=300)

# Graficar ambas curvas
plt.plot(x, y_x, label=r"$y = x$", color="blue", linewidth=2)
plt.plot(x, y_tan, label=r"$y = \tan(x)$", color="crimson", linewidth=2)

# Asíntotas verticales en x = pi/2 y x = 3*pi/2
plt.axvline(x=np.pi/2, color="gray", linestyle="--", alpha=0.7, label=r"Asíntotas de $\tan(x)$")
plt.axvline(x=3*np.pi/2, color="gray", linestyle="--", alpha=0.7)

# Marca de la solución encontrada x ≈ 4.4934
plt.plot(x_sol, x_sol, 'ro', markersize=8, label=rf"Solución ($x \approx {x_sol:.4f}$)")

# Delimitar límites de ejes
plt.ylim(-10, 10)
plt.xlim(0, 5)

# Nombre de ejes, títulos y leyenda
plt.xlabel("Eje $x$", fontsize=12)
plt.ylabel("Eje $y$", fontsize=12)
plt.title(r"Gráfica de $y = x$ y $y = \tan(x)$ en $[0, 5]$", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle=":")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper left", fontsize=10)

# Guardar la imagen para subir a la plataforma
plt.tight_layout()
plt.savefig("grafica_biseccion_tan.png", dpi=300)
plt.show()