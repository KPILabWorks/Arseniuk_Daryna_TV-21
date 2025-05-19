import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# 🔹 1. Завантаження CSV-файлу (вкажіть свій файл!)
df = pd.read_csv("phone_accelerometer_data.csv")  # Заміни на назву свого файлу

# 🔹 2. Перевірка структури
print(df.head())

# 🔹 3. Розрахунок загального прискорення (векторна сума x, y, z)
df['acc_total'] = np.sqrt(df['Accel_X_m_s2']**2 + df['Accel_Y_m_s2']**2 + df['Accel_Z_m_s2']**2)

# 🔹 4. Фільтрація шуму (опціонально: згладжування фільтром Савицького-Голея)
df['acc_filtered'] = savgol_filter(df['acc_total'], window_length=51, polyorder=3)

# 🔹 5. Побудова графіка
plt.figure(figsize=(14,6))
plt.plot(df['Time_s'], df['acc_total'], label='Сире прискорення', alpha=0.4)
plt.plot(df['Time_s'], df['acc_filtered'], label='Фільтроване прискорення', linewidth=2)
plt.xlabel("Час (с)")
plt.ylabel("Прискорення (m/s²)")
plt.title("Графік прискорення під час руху")
plt.legend()
plt.grid(True)
plt.show()

# 🔹 6. Розрахунок середнього прискорення
print("Середнє прискорення (сире):", df['acc_total'].mean())
print("Середнє прискорення (фільтроване):", df['acc_filtered'].mean())
