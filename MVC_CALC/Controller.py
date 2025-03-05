from Model import add, subtract, multiply, divide
from View import display_menu, get_user_input, display_result, display_error, ask_continue

def run_calculator():
    while True:
        display_menu()
        choice = input("Введите номер операции (1/2/3/4): ")

        num1, num2 = get_user_input()
        if num1 is None or num2 is None:
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            else:
                display_error("Неверный ввод. Пожалуйста, выберите номер операции от 1 до 4.")
                continue

            display_result(result)

        except ValueError as e:
            display_error(str(e))

        if not ask_continue():
            break
