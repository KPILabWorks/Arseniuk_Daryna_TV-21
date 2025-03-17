import pandas as pd
import dask.dataframe as dd
import numpy as np
import time

# Генерація великого набору даних
num_rows = 1_000_000  # 1 мільйон записів
df = pd.DataFrame({
    'id': np.arange(num_rows),
    'value': np.random.rand(num_rows),
    'category': np.random.choice(['A', 'B', 'C', 'D'], num_rows)
})

# Збереження у CSV для імітації роботи з великим файлом
df.to_csv('large_dataset.csv', index=False)

# 1. Оптимізоване читання великого файлу
print("Читання файлу...")
start_time = time.time()
df_large = pd.read_csv('large_dataset.csv', low_memory=False)  # Використання low_memory=False для кращої оптимізації
print(f"Час читання файлу: {time.time() - start_time:.2f} сек")

# Використання Dask для читання великих файлів
print("Читання файлу за допомогою Dask...")
start_time = time.time()
ddf = dd.read_csv('large_dataset.csv')
print(f"Час читання файлу Dask: {time.time() - start_time:.2f} сек")

# 2. Використання apply() та векторизованих функцій для обробки колонок

def transform_value(x):
    return x ** 2 + np.sin(x)  # Додаємо синусоїдну трансформацію

print("Обробка з .apply()...")
start_time = time.time()
df_large['transformed'] = df_large['value'].apply(transform_value)
print(f"Час виконання apply(): {time.time() - start_time:.2f} сек")

print("Обробка векторизованою функцією...")
start_time = time.time()
df_large['transformed_vec'] = df_large['value'] ** 2 + np.sin(df_large['value'])
print(f"Час виконання векторизованої функції: {time.time() - start_time:.2f} сек")

# 3. Порівняння швидкості пошуку по колонці
search_value = 500_000

print("Пошук за стандартним індексом...")
start_time = time.time()
result = df_large[df_large['id'] == search_value]
print(f"Час пошуку (без індексу): {time.time() - start_time:.5f} сек")

# Встановлення індексу та пошук
print("Пошук із set_index()...")
df_large = df_large.set_index('id')
start_time = time.time()
result = df_large.loc[search_value]
print(f"Час пошуку (з set_index()): {time.time() - start_time:.5f} сек")
