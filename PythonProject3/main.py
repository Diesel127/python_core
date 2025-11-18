def process_input(value):
    if value == "":
        return "Ошибка: введена пустая строка."

    try:
        num = int(value)
        return num * num
    except ValueError:
        return "Ошибка: введенная строка не является числом."

print(process_input("5"))
print(process_input(" "))