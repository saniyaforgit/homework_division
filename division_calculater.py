def division_calculator():
    try:
        a = float(input("Введите число a: "))
        b = float(input("Введите число b: "))
        result = a / b
        print("Результат:", result)
    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    finally:
        print("Завершено")

# вызов функции
if __name__ == "__main__":
    division_calculator()




