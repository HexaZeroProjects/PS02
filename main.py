import requests
import pprint

# Задание 1: Получение данных
print("=============================")
print("Задание 1: Получение данных")
params = {
    'q' : 'html',
}

response = requests.get('https://api.github.com/search/repositories', params=params)
print(response.status_code)
print(response.ok)

if response.ok:
    print ('запрос успешно выполнен')
    response_json = response.json()
    print(f"количество результатов html: {response.json()['total_count']}")
    pprint.pprint(response_json)
else:
    print ('произошла ошибка')

# Задание 2: Параметры запроса
print("=============================")
print("Задание 2: Параметры запроса")

url = 'https://jsonplaceholder.typicode.com/posts'
params = {'userId': 1}

# Отправка GET-запроса с тайм-аутом в 5 секунд
try:
    print("Отправка запроса...")
    response = requests.get(url, params=params, timeout=5)
    print(f"Запрос отправлен, код ответа: {response.status_code}")

    # Проверка статуса запроса
    if response.status_code == 200:
        # Получение данных в формате JSON
        data = response.json()

        # Проверка, есть ли данные
        if data:
            print("Получены данные:")
            pprint.pprint(data)
        else:
            print("Данные не получены, ответ пуст.")
    else:
        print(f"Ошибка: {response.status_code}")
except requests.exceptions.Timeout:
    print("Ошибка: Превышено время ожидания.")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")

# Задание 3: Отправка данных
print("=============================")
print("Задание 3: Отправка данных")
# URL для POST-запроса
url = 'https://jsonplaceholder.typicode.com/posts'

# Данные для отправки
data = {'title': 'foo', 'body': 'bar', 'userId': 1}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Проверка статуса и вывод ответа
print(f"Статус-код: {response.status_code}")
print("Ответ от сервера:")
pprint.pprint(response.json())