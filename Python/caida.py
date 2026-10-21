from collections.abc import Callable
import numpy as np
import matplotlib.pyplot as plt

def s(t: float) -> float:
    so = 300
    g = 9.8
    m = 0.25
    k = 0.1
    return (so - (g * m / k) * t) + ((m**2 * g) / (k**2)) * (1 - np.exp(-k * t / m))


def biseccion(s: Callable[[float], float], a: float, b: float, TOL=1e-6, N0=100):
    """Devuelve (p, historia), con historia = [(a, b, p) por iteración]."""
    FA = s(a)
    historia = []
    i = 1
    while i <= N0:
        p = a + (b - a) / 2                    # Punto medio estable
        FP = s(p)
        historia.append((a, b, p))             # Guarda el registro (a, b, p)
        
        if FP == 0 or (b - a) / 2 < TOL:       # Parada por tolerancia o raíz exacta
            return p, historia
            
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            
    raise RuntimeError(f"fracasó después de {N0} iteraciones")


def mostrar_resultados(historia: list, raiz: float):
    print(f"Raíz aproximada encontrada (t*): {raiz:.8f}\n")
    print(f"{'Iteración':<10} | {'a':<12} | {'b':<12} | {'p (Punto Medio)':<15}")
    print("-" * 58)
    for idx, (a_val, b_val, p_val) in enumerate(historia, 1):
        print(f"{idx:<10} | {a_val:<12.6f} | {b_val:<12.6f} | {p_val:<15.6f}")


def graficar(t_star, historia, k_iteracion, archivo="caida.png"):
    """Dibuja s(t) en [0, 20] con nombres de ejes y título. 
    Resalta el intervalo [a, b] de la iteración indicada y su punto medio p, 
    además de marcar el punto (t*, 0)."""
    t = np.linspace(0, 20, 400)
    plt.figure(figsize=(9, 4.5))
    plt.plot(t, s(t), label="s(t)")
    plt.axhline(0, color="gray", linestyle="--", linewidth=1)
    
    # Resaltar la iteración solicitada (ej. iteración 3 -> intervalo [10, 15])
    if k_iteracion is not None and k_iteracion <= len(historia):
        a, b, p = historia[k_iteracion - 1]
        plt.axvspan(a, b, color="green", alpha=0.25,
                    label=f"Iter {k_iteracion}: [{a:.2f}, {b:.2f}] (p={p:.2f})")
        plt.axvline(p, color="green", linestyle=":", linewidth=1, label=f"Punto medio = {p}")
        
    # Marcar el punto (t*, 0) de la raíz encontrada
    plt.plot(t_star, 0, "ro", label=f"t* = {t_star:.4f}")
    
    plt.xlabel("Tiempo t (s)")
    plt.ylabel("Posición s(t) (m)")
    plt.title("Curva s(t) en [0, 20] - Método de Bisección")
    plt.legend()
    plt.grid(True)
    plt.savefig(archivo, dpi=150)
    plt.show()



raiz, historia = biseccion(s, 0, 20, TOL=10**(-4))
mostrar_resultados(historia, raiz)
    
graficar(raiz, historia, k_iteracion=3, archivo="caida.png")