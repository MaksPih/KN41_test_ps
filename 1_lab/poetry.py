import requests

# Отримання даних з API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Перевірка статусу відповіді
if response.status_code == 200:
    posts = response.json()
    print("Список постів:")
    for post in posts[:5]:  # Виводимо перші 5 постів
        print(f"Post ID: {post['id']}, Title: {post['title']}")
else:
    print("Не вдалося отримати дані з API")