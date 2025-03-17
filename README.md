# Arseniuk_Daryna_TV-21
# Варіант 1
# Практична 1
# Лічильник символів у рядку

## Опис
Ця програма приймає рядок від користувача та повертає словник, де ключі — це унікальні символи, а значення — кількість їх входжень у рядку.

## Використання
1. Запустіть програму.
2. Введіть будь-який рядок у консоль.
3. Отримайте словник із підрахунком входжень кожного символу.

## Приклад роботи
Вхід:
```
Введіть рядок: hello
```
Вихід:
```
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

## Вимоги
- Python 3.x

## Ліцензія
Цей код можна використовувати та змінювати без обмежень.

# Практична 2

# Оптимізація роботи з великими наборами даних у Pandas та Dask

Цей проєкт демонструє ефективну роботу з великими наборами даних (>1 млн записів) у Python за допомогою бібліотек Pandas та Dask. Він містить приклади читання великих файлів, обробки колонок із застосуванням `apply()` та векторизованих функцій, а також порівняння швидкості пошуку даних при стандартному індексі та `set_index()`.

## Вимоги
Перед запуском переконайтеся, що у вас встановлені необхідні бібліотеки:
```sh
pip install pandas dask numpy
```

## Опис коду
### 1. Генерація великого набору даних
Створюється датафрейм `df` із 1 мільйоном записів, що містить три колонки:
- `id` – унікальний ідентифікатор
- `value` – випадкове значення
- `category` – випадкова категорія ('A', 'B', 'C', 'D')

Цей набір даних зберігається у `large_dataset.csv` для імітації роботи з великими файлами.

### 2. Читання великого файлу
Використовуються два підходи:
- **Pandas**: стандартне читання CSV (`pd.read_csv()`)
- **Dask**: оптимізоване читання великих файлів (`dd.read_csv()`)

### 3. Обробка колонок
Демонструється використання:
- `.apply()`: застосування функції до кожного значення в колонці
- Векторизованих функцій: оптимізоване обчислення без використання `.apply()`

### 4. Порівняння швидкості пошуку даних
Виконується пошук значення у колонці `id` двома способами:
- Без індексу (`df[df['id'] == value]`)
- Після встановлення індексу (`df.set_index('id').loc[value]`)

## Використання
Запустіть скрипт:
```sh
python script.py
```
Він створить файл `large_dataset.csv`, завантажить його та виконає всі операції, виводячи час виконання кожного кроку.


## Ліцензія
Цей проєкт має відкриту ліцензію MIT.

# Практична 3
# Реалізація алгоритму обчислення енергетичних потреб

## Опис проєкту
Цей проєкт реалізує алгоритм для обчислення енергетичних потреб на основі даних з датчиків. Використовується оптимізація за допомогою бібліотеки `Numba` для прискорення обчислень. Продуктивність оптимізованої версії порівнюється з чистою реалізацією Python, а результати візуалізуються за допомогою графіка.

## Функціональність
- Генерація тестових даних, що включають потужність, температуру та інші фактори.
- Реалізація обчислення енергетичних потреб у чистому Python.
- Оптимізована версія обчислення з використанням `Numba`.
- Порівняння продуктивності обох реалізацій на наборах даних різного розміру.
- Побудова графіка часу виконання для кожної реалізації.

## Використані технології
- Python 3
- `NumPy` – для роботи з масивами числових даних
- `Numba` – для прискорення обчислень
- `Matplotlib` – для візуалізації результатів

## Вимоги до середовища
Перед запуском необхідно встановити необхідні бібліотеки. Використовуйте наступну команду:

```sh
pip install numpy numba matplotlib
```

## Запуск програми
Запустіть скрипт `main.py` для виконання обчислень та побудови графіка:

```sh
python main.py
```

## Результати
Програма виводить графік порівняння продуктивності чистого Python і оптимізованого варіанту з `Numba`. Очікується значне прискорення роботи при збільшенні розміру вхідних даних.






