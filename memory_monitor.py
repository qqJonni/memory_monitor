import psutil
import requests
import time

# Задайте пороговое значение для потребления памяти (в байтах)
threshold_memory = 500000000  # Например, 500 МБ (500 * 1024 * 1024 байт)

# Задайте URL API, на который будет отправлен запрос в случае превышения порогового значения
api_url = "https://httpbin.org/post"

while True:
    # Получите текущее потребление памяти
    current_memory = psutil.virtual_memory().used

    # Сравните текущее потребление памяти с пороговым значением
    if current_memory > threshold_memory:
        # Отправьте HTTP-запрос на API
        response = requests.post(api_url, json={"message": "Memory threshold exceeded", "memory_used": current_memory})
        response.raise_for_status()

        # Проверьте статус кода ответа
        if response.ok:
            print("HTTP запрос успешно отправлен.")
        else:
            print(f"Ошибка отправки HTTP запроса. Код ответа: {response.status_code}")

    # Подождите некоторое время перед повторной проверкой (например, 5 минут)
    time.sleep(300)  # 300 секунд = 5 минут
