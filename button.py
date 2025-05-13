from abc import ABC, abstractmethod

# Абстрактный класс кнопки
class Button(ABC):
    @abstractmethod
    def press(self):
        pass

# Конкретные классы кнопок
class DigitButton(Button):
    def __init__(self, digit):
        self._digit = digit

    def press(self):
        return str(self._digit)

class OperatorButton(Button):
    def __init__(self, operation):
        self._operation = operation

    def press(self):
        return self._operation

class EqualsButton(Button):
    def press(self):
        return "="

class ClearButton(Button):
    def press(self):
        return "C"

class PercentButton(Button):
    def press(self):
        return "%"

# Абстрактный класс фабрики кнопок
class ButtonFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

# Конкретные классы фабрик
class DigitButtonFactory(ButtonFactory):
    def __init__(self, digit):
        self._digit = digit

    def create_button(self):
        return DigitButton(self._digit)

class OperatorButtonFactory(ButtonFactory):
    def __init__(self, operation):
        self._operation = operation

    def create_button(self):
        return OperatorButton(self._operation)

class EqualsButtonFactory(ButtonFactory):
    def create_button(self):
        return EqualsButton()

class ClearButtonFactory(ButtonFactory):
    def create_button(self):
        return ClearButton()

class PercentButtonFactory(ButtonFactory):
    def create_button(self):
        return PercentButton()