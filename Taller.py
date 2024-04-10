import numpy as np
import matplotlib.pyplot as plt

# Definir la función exponencial
def exp_taylor(x, n):
    return np.sum([(x**i) / np.math.factorial(i) for i in range(n)])

# Definir la función seno
def sin_taylor(x, n):
    return np.sum([((-1)**i) * (x**(2*i + 1)) / np.math.factorial(2*i + 1) for i in range(n)])

# Definir la función coseno
def cos_taylor(x, n):
    return np.sum([((-1)**i) * (x**(2*i)) / np.math.factorial(2*i) for i in range(n)])

# Definir la función tangente (como el cociente entre seno y coseno)
def tan_taylor(x, n):
    return sin_taylor(x, n) / cos_taylor(x, n)

# Definir la función logaritmo natural alrededor de x=1
def log_taylor(x, n):
    return np.sum([((-1)**(i+1)) * ((x-1)**(i)) / i for i in range(1, n+1)])

# Definir el rango de x
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# Calcular las aproximaciones para cada función
y_approx_3 = [exp_taylor(i, 3) for i in x]
y_approx_5 = [exp_taylor(i, 5) for i in x]
y_approx_10 = [exp_taylor(i, 10) for i in x]
y_approx_20 = [exp_taylor(i, 20) for i in x]
y_sin_approx = [sin_taylor(i, 5) for i in x]
y_cos_approx = [cos_taylor(i, 5) for i in x]
y_tan_approx = [tan_taylor(i, 5) for i in x]
y_log_approx = [log_taylor(i, 5) for i in x]

# Calcular las funciones reales
y_real_exp = np.exp(x)
y_real_sin = np.sin(x)
y_real_cos = np.cos(x)
y_real_tan = np.tan(x)
y_real_log = np.log(x)

# Graficar las aproximaciones y las funciones reales
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y_real_sin, label='Seno Real')
plt.plot(x, y_sin_approx, label='Aproximación')
plt.legend()
plt.title('Aproximación del Seno con Series de Taylor')

plt.subplot(2, 2, 2)
plt.plot(x, y_real_cos, label='Coseno Real')
plt.plot(x, y_cos_approx, label='Aproximación')
plt.legend()
plt.title('Aproximación del Coseno con Series de Taylor')

plt.subplot(2, 2, 3)
plt.plot(x, y_real_tan, label='Tangente Real')
plt.plot(x, y_tan_approx, label='Aproximación')
plt.legend()
plt.title('Aproximación de la Tangente con Series de Taylor')

plt.subplot(2, 2, 4)
plt.plot(x, y_real_log, label='Logaritmo Real')
plt.plot(x, y_log_approx, label='Aproximación')
plt.legend()
plt.title('Aproximación del Logaritmo con Series de Taylor')

plt.tight_layout()
plt.show()
