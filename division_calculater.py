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

# import pandas as pd

# class Product:
#     def __init__(self, title, price, quantity):
#         self.title = title
#         self.price = price
#         self.quantity = quantity

#     def line_total(self):
#         return self.price * self.quantity


# def excel_report():
#     df = pd.read_excel("products.xlsx")

#     report_rows = []
#     total_sum = 0

#     for _, row in df.iterrows():
#         try:
#             title = row["Title"]
#             price = float(row["Price"])
#             quantity = float(row["Quantity"])

#             product = Product(title, price, quantity)
#             line_total = product.line_total()

#             report_rows.append({"Title": title, "LineTotal": line_total})
#             total_sum += line_total

#         except (ValueError, TypeError):
#             continue

#     report_rows.append({"Title": "TOTAL", "LineTotal": total_sum})

#     report_df = pd.DataFrame(report_rows)
#     report_df.to_excel("products_report.xlsx", index=False)

#     print("Отчёт сформирован")


# if __name__ == "__main__":
#     excel_report()

# -----Задание 3 — Excel: студенты и средний балл------


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.scores = []

#     def add_score(self, score):
#         self.scores.append(score)

#     def avg(self):
#         if not self.scores:
#             return 0
#         return sum(self.scores) / len(self.scores)

# import pandas as pd

# def student_report():
#     df = pd.read_excel("students2.xlsx")

#     report_rows = []

#     for _, row in df.iterrows():
#         student = Student(row["Name"])
#         for col in ["Score1", "Score2", "Score3"]:
#             try:
#                 score = float(row[col])
#                 student.add_score(score)
#             except (ValueError, TypeError):
#                 continue  # пропускаем "грязные" значения

#         report_rows.append({"Name": student.name, "Avg": student.avg()})

#     report_df = pd.DataFrame(report_rows)
#     report_df.to_excel("report_students.xlsx", index=False)
#     print("Отчёт по студентам сформирован")

