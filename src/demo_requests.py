import json
import requests
import logging
from logger_config import setup_logging

logger = setup_logging()

def get_data():
    logger.info("Начинаем запрос к API...")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=5)
        response.raise_for_status()
        data = response.json() # Используем метод json из requests
        logger.info(f"Получены данные: {data}")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    get_data()