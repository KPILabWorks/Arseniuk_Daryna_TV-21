import numpy as np
import time
import matplotlib.pyplot as plt
from numba import jit


# Генерація тестових даних
def generate_data(size):
    power = np.random.uniform(100, 1000, size)  # Потужність у Ватах
    temperature = np.random.uniform(-10, 40, size)  # Температура в градусах Цельсія
    other_factors = np.random.uniform(0.5, 1.5, size)  # Додаткові фактори (коефіцієнти)
    return power, temperature, other_factors


# Чиста Python-реалізація

def energy_needs_python(power, temperature, factors):
    energy = []
    for p, t, f in zip(power, temperature, factors):
        adj_factor = 1.0 + (t / 100.0)  # Вплив температури
        energy.append(p * f * adj_factor)
    return energy


# Оптимізована реалізація з Numba
@jit(nopython=True)
def energy_needs_numba(power, temperature, factors):
    size = len(power)
    energy = np.empty(size)
    for i in range(size):
        adj_factor = 1.0 + (temperature[i] / 100.0)
        energy[i] = power[i] * factors[i] * adj_factor
    return energy


# Оцінка продуктивності
sizes = [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]
time_python = []
time_numba = []

for size in sizes:
    power, temp, factors = generate_data(size)

    # Чистий Python
    start = time.time()
    energy_needs_python(power, temp, factors)
    time_python.append(time.time() - start)

    # Numba
    start = time.time()
    energy_needs_numba(power, temp, factors)
    time_numba.append(time.time() - start)

# Побудова графіку
plt.figure(figsize=(10, 5))
plt.plot(sizes, time_python, label='Python', marker='o')
plt.plot(sizes, time_numba, label='Numba', marker='s')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Розмір вхідних даних')
plt.ylabel('Час виконання (сек)')
plt.title('Порівняння продуктивності: чистий Python vs Numba')
plt.legend()
plt.grid(True)
plt.show()
