import pickle

# Пример объекта для сериализации
data = {'name': 'Alice', 'age': 30, 'is_student': False}

# Сериализация объекта в файл
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

# Десериализация объекта из файла
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)