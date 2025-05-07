import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2E2E2E")

        self.expression = ""
        self.result_var = tk.StringVar()

        # Дисплей
        self.display = ttk.Entry(
            root, textvariable=self.result_var, font=("Arial", 20), justify="right", state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        # Стили кнопок
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14), padding=10)

        # Кнопки
        buttons = [
            ('7', 1, 0, "#424242"), ('8', 1, 1, "#424242"), ('9', 1, 2, "#424242"), ('/', 1, 3, "#F44336"),
            ('4', 2, 0, "#424242"), ('5', 2, 1, "#424242"), ('6', 2, 2, "#424242"), ('*', 2, 3, "#F44336"),
            ('1', 3, 0, "#424242"), ('2', 3, 1, "#424242"), ('3', 3, 2, "#424242"), ('-', 3, 3, "#F44336"),
            ('0', 4, 0, "#424242"), ('.', 4, 1, "#424242"), ('+', 4, 2, "#F44336"), ('=', 4, 3, "#4CAF50")
        ]

        # Размещение кнопок
        for (text, row, col, bg) in buttons:
            button = ttk.Button(
                root, text=text, style="TButton",
                command=lambda t=text: self.button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            button.configure(style=f"{text}.TButton")
            style.configure(f"{text}.TButton", background=bg)

        # Адаптивность
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Ошибка"
        else:
            self.expression += char
        self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()