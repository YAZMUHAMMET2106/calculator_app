import tkinter as tk
from tkinter import ttk
import sys

print("Запуск calculator_app.py...")  # Отладочный вывод

try:
    from button import (ButtonFactory, DigitButtonFactory, OperatorButtonFactory,
                        EqualsButtonFactory, ClearButtonFactory, PercentButtonFactory)
except ImportError as e:
    print(f"Ошибка импорта модуля button: {e}")
    print("Убедитесь, что файл button.py находится в той же папке.")
    sys.exit(1)

class CalculatorApp:
    def __init__(self, root):
        print("Инициализация CalculatorApp...")  # Отладочный вывод
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self.root.configure(bg="#333333")

        self.expression = ""
        self.display_var = tk.StringVar()

        # Дисплей
        try:
            display = ttk.Entry(root, textvariable=self.display_var, font=("Arial", 18), justify="right")
            display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        except Exception as e:
            print(f"Ошибка создания дисплея: {e}")
            sys.exit(1)

        # Стили кнопок
        try:
            style = ttk.Style()
            style.configure("TButton", font=("Arial", 14), padding=10)
        except Exception as e:
            print(f"Ошибка настройки стилей: {e}")
            sys.exit(1)

        # Определение кнопок с использованием фабрик
        button_configs = [
            (ClearButtonFactory(), 1, 0, "#555555"),
            (OperatorButtonFactory("("), 1, 1, "#2196F3"),
            (OperatorButtonFactory(")"), 1, 2, "#2196F3"),
            (OperatorButtonFactory("/"), 1, 3, "#FF9800"),
            (DigitButtonFactory(7), 2, 0, "#555555"),
            (DigitButtonFactory(8), 2, 1, "#555555"),
            (DigitButtonFactory(9), 2, 2, "#555555"),
            (OperatorButtonFactory("*"), 2, 3, "#FF9800"),
            (DigitButtonFactory(4), 3, 0, "#555555"),
            (DigitButtonFactory(5), 3, 1, "#555555"),
            (DigitButtonFactory(6), 3, 2, "#555555"),
            (OperatorButtonFactory("-"), 3, 3, "#FF9800"),
            (DigitButtonFactory(1), 4, 0, "#555555"),
            (DigitButtonFactory(2), 4, 1, "#555555"),
            (DigitButtonFactory(3), 4, 2, "#555555"),
            (OperatorButtonFactory("+"), 4, 3, "#FF9800"),
            (DigitButtonFactory(0), 5, 0, "#555555"),
            (OperatorButtonFactory("."), 5, 1, "#555555"),
            (PercentButtonFactory(), 5, 2, "#555555"),
            (EqualsButtonFactory(), 5, 3, "#4CAF50"),
        ]

        for factory, row, col, bg in button_configs:
            try:
                button = factory.create_button()
                style_name = f"{button.press()}.TButton"
                style.configure(style_name, font=("Arial", 14), padding=10, background=bg)
                ttk.Button(
                    root, text=button.press(), style=style_name,
                    command=lambda b=button: self.button_click(b.press())
                ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            except Exception as e:
                print(f"Ошибка при создании кнопки {button.press()}: {e}")

        # Настройка сетки
        try:
            for i in range(6):
                self.root.grid_rowconfigure(i, weight=1)
            for i in range(4):
                self.root.grid_columnconfigure(i, weight=1)
        except Exception as e:
            print(f"Ошибка настройки сетки: {e}")
            sys.exit(1)

        try:
            self.root.bind("<Key>", self.key_press)
        except Exception as e:
            print(f"Ошибка привязки клавиш: {e}")
            sys.exit(1)

    def button_click(self, char):
        try:
            if char == 'C':
                self.expression = ""
            elif char == '=':
                self.expression = str(eval(self.expression))
            elif char == '%':
                self.expression = str(eval(self.expression) / 100)
            else:
                self.expression += char
            self.display_var.set(self.expression)
        except Exception as e:
            self.expression = f"Ошибка: {e}"
            self.display_var.set(self.expression)

    def key_press(self, event):
        try:
            if event.char in '0123456789+-*/.()':
                self.button_click(event.char)
            elif event.keysym == 'Return':
                self.button_click('=')
            elif event.keysym == 'Escape':
                self.button_click('C')
            elif event.keysym == 'BackSpace':
                self.expression = self.expression[:-1]
                self.display_var.set(self.expression)
            elif event.char == '%':
                self.button_click('%')
        except Exception as e:
            self.display_var.set(f"Ошибка: {e}")

if __name__ == "__main__":
    print("Создание окна tkinter...")  # Отладочный вывод
    try:
        root = tk.Tk()
        app = CalculatorApp(root)
        print("Запуск главного цикла...")  # Отладочный вывод
        root.mainloop()
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
        sys.exit(1)