def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        print("Ошибка: деление на ноль")
        return None
    return a / b


def calculator():
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")

    while True:
        choice = input("Выберите операцию (введите соответствующую цифру): ")

        if choice == "0":
            print("Выход из программы")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Ошибка: некорректный выбор операции")
            continue

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Результат сложения: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Результат вычитания: {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Результат умножения: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is not None:
                print(f"Результат деления: {result}")


calculator()
