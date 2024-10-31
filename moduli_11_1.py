import requests

# Отправляем GET-запрос к URL
response = requests.get('https://www.example.com')

# Выводим статус-код ответа
print(response.status_code)

# Отправляем POST-запрос к URL с данными
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://www.example.com', data=data)

# Выводим текст ответа
print(response.text)

# Отправляем PUT-запрос к URL с данными
data = {'key1': 'new_value1', 'key2': 'new_value2'}
response = requests.put('https://www.example.com', data=data)

# Выводим текст ответа
print(response.text)

# Отправляем DELETE-запрос к URL
response = requests.delete('https://www.example.com')

# Выводим статус-код ответа
print(response.status_code)
