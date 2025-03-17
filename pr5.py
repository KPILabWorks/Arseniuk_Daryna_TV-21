import pandas as pd

# Приклад часового ряду з правильними даними
values = [10, 12, 14, 13, 15, 18, 19, 21, 23, 22, 25, 30, 35, 32, 40, 42, 45, 49, 50, 55, 60, 59, 70, 65, 80, 85, 90, 110, 120, 125] * 3 + [500]
dates = pd.date_range(start='2022-01-01', periods=len(values), freq='D')  # Генеруємо дати стільки ж, скільки значень у `values`

# Перевірка довжини
print(len(dates), len(values))  # Має бути однакова кількість

# Створюємо DataFrame
data = {
    'date': dates,
    'value': values
}

df = pd.DataFrame(data)

# Обчислюємо квартилі та IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

# Визначаємо межі для аномалій
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Фільтруємо аномальні значення
anomalies = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]

# Виводимо аномальні значення
print("Аномальні значення:")
print(anomalies)
