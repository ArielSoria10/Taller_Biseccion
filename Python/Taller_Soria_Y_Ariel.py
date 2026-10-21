import matplotlib.pyplot as plt
import numpy as np

def f(x:float)->float:
    return x**3+4*x**2-10



def biseccion( f: callable[float,float], a: float, b: float, TOL=1e-6, N0=100):
    """Devuelve (p, historia), con historia = [(a, b, p) por iteración]."""
    FA = f(a)
    historia = []
    i = 1
    while i <= N0:
        p = a+(b-a)/ 2                                     # COMPLETE: punto medio estable
        FP = f(p)
        historia.append((a, b, p))                        # COMPLETE: (a, b, p)
        if FP == 0 or (b - a)/2 < TOL:   
            return p, historia
        i = i + 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    raise RuntimeError(f"fracasó después de {N0} iteraciones")

def mostrar_resultados(historia: list, raiz: float):
    print(f"Raíz aproximada encontrada: {raiz:.8f}\n")
    print(f"{'Iteración':<6} | {'a':<12} | {'b':<12} | {'p (Punto Medio)':<15}")
    print("-" * 55)
    for idx, (a_val, b_val, p_val) in enumerate(historia, 1):
        print(f"{idx:<6} | {a_val:<12.6f} | {b_val:<12.6f} | {p_val:<15.10f}")



raiz, historia = biseccion(f, 1, 2, TOL=10**(-2))
mostrar_resultados(historia, raiz)



