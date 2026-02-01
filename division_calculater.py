# Задание 1 — Калькулятор деления (исключения)
# 
# def division_calculator():
#     try:
#         a = float(input("Введите число a: "))
#         b = float(input("Введите число b: "))
#         result = a / b
#         print("Результат:", result)
#     except ValueError:
#         print("Ошибка: введено не число")
#     except ZeroDivisionError:
#         print("Ошибка: деление на ноль")
#     finally:
#         print("Завершено")

# # вызов функции
# if __name__ == "__main__":
#     division_calculator()

# ------Задание 2 — Excel: товары и отчёт-------

import pandas as pd

class Product:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity

    def line_total(self):
        return self.price * self.quantity


def excel_report():
    df = pd.read_excel("products.xlsx")

    report_rows = []
    total_sum = 0

    for _, row in df.iterrows():
        try:
            title = row["Title"]
            price = float(row["Price"])
            quantity = float(row["Quantity"])

            product = Product(title, price, quantity)
            line_total = product.line_total()

            report_rows.append({"Title": title, "LineTotal": line_total})
            total_sum += line_total

        except (ValueError, TypeError):
            continue

    report_rows.append({"Title": "TOTAL", "LineTotal": total_sum})

    report_df = pd.DataFrame(report_rows)
    report_df.to_excel("products_report.xlsx", index=False)

    print("Отчёт сформирован")


if __name__ == "__main__":
    excel_report()
