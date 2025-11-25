import pickle

# Пример словаря для сериализации
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}


# Напишите тут ваш код
serial_data = pickle.dumps(data)
loaded_data = pickle.loads(serial_data)
print(loaded_data)