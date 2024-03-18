# добавить обработку ValueError
def string_to_int(s = 'puma'):
    try:
        return int(s)
    except ValueError:
        return print(f"Невозможно преобразовать '{s}' в целое число")
string_to_int()


# добавить обработку FileNotFoundError, IOError
def read_file(filename = 'text.txt'):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return print(f"Файл '{filename}' не найден")
    except IOError:
        print(f"Ошибка ввода/ввыда при работе с файлом '{filename}'")
read_file()


# добавить обработку ZeroDivisionError, TypeError
def divide_numbers(a = 5, b = 'с'):
    try:
        return a / b
    except ZeroDivisionError:
        return print('Делить на ноль нельзя')
    except TypeError:
        return print('Неверный тип переменной')
divide_numbers()


# добавить обработку IndexError, TypeError
def access_list_element(lst = 'puma', index = '300'):
    try:
        return lst[index]
    except IndexError:
        print(f"Индекс строки '{index}' за пределами")
    except TypeError:
        return print(f"Неверный тип переменной '{index}'")
access_list_element()