def count_chars(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Отримуємо введення від користувача
text = input("Введіть рядок: ")

# Викликаємо функцію і друкуємо результат
result = count_chars(text)
print(result)
