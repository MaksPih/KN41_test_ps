class Name:
    def __init__(self, name, hobby) -> None:
        allowed_names = ["Богдан", "Анонім", "Максим"] 

        if name not in allowed_names:
            raise ValueError("Дозволені імена: Богдан, Анонім, Максим")

        if not hobby.strip(): 
            raise ValueError("Поле 'хобі' не може бути порожнім!")

        self.name = name
        self.hobby = hobby

    def __str__(self):
        return f"Ім’я: {self.name}, Хобі: {self.hobby}"
    
try:
    # 1. Правильні дані
    a = Name("Максим", "Футбол")
    print(a)

    # 2. Неправильне ім’я
    b = Name("Бодько", "Читання")

    # 3. Порожнє хобі
    c = Name("Максим", "")
except ValueError as e:
    print("❌ Помилка:", e)