def display_menu():
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

def get_user_input():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        return num1, num2
    except ValueError:
        print("Ошибка! Пожалуйста, введите числовое значение.")
        return None, None

def display_result(result):
    print(f"Результат: {result}")

def display_error(message):
    print(message)

def ask_continue():
    return input("Хотите выполнить еще один расчет? (да/нет): ").lower() == 'да'
