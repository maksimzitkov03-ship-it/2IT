result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Некоректний тип даних для виконання операції")
    if a < b:
        raise ValueError("Число a менше за b")
    if b > 100:
        raise IndexError("Число b більше за 100")
    return a / b

data = [(10, 2), (2, 5), ("123", 4), (18, 0), ([], 15), (8, 4)]

for key, value in data:
    try:
        res = divider(key, value)
        result.append(res)
    except ZeroDivisionError:
        print(f"Помилка: Спроба ділення на нуль! Елементи: a = {key}, b = {value}")
    except ValueError as e:
        print(f"Помилка [ValueError]: {e}! Елементи: a = {key}, b = {value}")
    except IndexError as e:
        print(f"Помилка [IndexError]: {e}! Елементи: a = {key}, b = {value}")
    except TypeError as e:
        print(f"Помилка [TypeError]: {e}! Елементи: a = {key}, b = {value}")
    except Exception as e:
        print(f"Виникла інша помилка: {e}")

print("\nКінцевий список успішних результатів:")
print(result)
