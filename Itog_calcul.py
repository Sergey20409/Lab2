# TODO опишите здесь функции для решения задачи
print("Вот твой калькулятор")

# Ввод числа
def get_num(perem):
    while True:
        try:
            number = float(input(perem))
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            print("Это не число! Введите число.")

# выбор действия
def get_operat():
    mess = "Выберите действие (+, -, *, /): "
    correct_operations = '+-/*'
    operat = input(mess)

    while operat not in correct_operations:
        print('Нет такого действия. Повторите попытку.')
        operat = input(mess)
    return operat

# Расчёт
def calculate(num1, num2, operat):
    result = None
    if operat == '+':
        result = num1 + num2
    elif operat == '-':
        result = num1 - num2
    elif operat == '/':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "На ноль делить нельзя"
    elif operat == '*':
        result = num1 * num2
    return result

# Вывод результата
def main():
    num1 = get_num("Введите первое число: ")
    num2 = get_num("Введите второе число: ")
    operat = get_operat() # выбор действия
    result = calculate(num1, num2, operat) # результат
    print("Результат:", result) # вывод результата

main()

# if __name__ == '__main__':
#     # TODO запустите здесь все необходимые функции



