import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def energy_flow(t, y, A, P):
    return A @ y + P

def simulate_energy_network(A, P, y0, t_span, t_eval):
    sol = solve_ivp(energy_flow, t_span, y0, args=(A, P), t_eval=t_eval, method='RK45')
    return sol

# Визначення параметрів мережі
n = 5  # кількість вузлів
np.random.seed(42)
A = -np.diag(np.ones(n)) + np.random.rand(n, n) * 0.1  # Динамічна матриця
P = np.random.rand(n) - 0.5  # Вектор збурень

y0 = np.zeros(n)  # Початкові умови

t_span = (0, 10)
t_eval = np.linspace(*t_span, 100)

sol = simulate_energy_network(A, P, y0, t_span, t_eval)

# Візуалізація
plt.figure(figsize=(10, 5))
for i in range(n):
    plt.plot(sol.t, sol.y[i], label=f'Node {i+1}')
plt.xlabel('Time')
plt.ylabel('Energy Flow')
plt.title('Energy Flow Simulation in a Network')
plt.legend()
plt.grid()
plt.show()

# Аналіз стабільності: перевірка власних значень
eig_values = np.linalg.eigvals(A)
stability = np.all(np.real(eig_values) < 0)
print(f'System is stable: {stability}')
