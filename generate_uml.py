def generate_uml():
    uml = """
@startuml
abstract class Button {
    +press(): str
}

class DigitButton {
    -_digit: int
    +press(): str
}

class OperatorButton {
    -_operation: str
    +press(): str
}

class EqualsButton {
    +press(): str
}

class ClearButton {
    +press(): str
}

class PercentButton {
    +press(): str
}

abstract class ButtonFactory {
    +create_button(): Button
}

class DigitButtonFactory {
    -_digit: int
    +create_button(): Button
}

class OperatorButtonFactory {
    -_operation: str
    +create_button(): Button
}

class EqualsButtonFactory {
    +create_button(): Button
}

class ClearButtonFactory {
    +create_button(): Button
}

class PercentButtonFactory {
    +create_button(): Button
}

Button <|.. DigitButton
Button <|.. OperatorButton
Button <|.. EqualsButton
Button <|.. ClearButton
Button <|.. PercentButton

ButtonFactory <|.. DigitButtonFactory
ButtonFactory <|.. OperatorButtonFactory
ButtonFactory <|.. EqualsButtonFactory
ButtonFactory <|.. ClearButtonFactory
ButtonFactory <|.. PercentButtonFactory

DigitButtonFactory --> DigitButton
OperatorButtonFactory --> OperatorButton
EqualsButtonFactory --> EqualsButton
ClearButtonFactory --> ClearButton
PercentButtonFactory --> PercentButton
@enduml
    """
    print("Текст UML-диаграммы:\n")
    print(uml)
    print("\nСкопируйте текст выше и вставьте в PlantUML (например, http://www.plantuml.com/plantuml) для визуализации.")
    print("Или используйте расширение PlantUML в VS Code для просмотра диаграммы.")
    return uml

if __name__ == "__main__":
    generate_uml()