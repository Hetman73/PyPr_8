import logging
import requests

# Получаем логгер для этого модуля. Настройка будет в main.py
logger = logging.getLogger(__name__)


def fetch_vacancies(search_query: str = "python") -> list:
    """
    Делает запрос к API Himalayas и возвращает список вакансий.
    """
    logger.info(f"Запрос вакансий по слову: '{search_query}'")

    url = "https://himalayas.app/jobs/api"

    # Параметры запроса. Himalayas использует 'q' для поиска
    params = {
        "q": search_query,
        "limit": 50  # Ограничим количество, чтобы не грузить всё сразу
    }

    try:
        # Отправляем GET-запрос
        response = requests.get(url, params=params, timeout=30)

        # Проверяем, что запрос прошел успешно (код 200)
        response.raise_for_status()

        # Превращаем ответ в словарь Python
        data = response.json()

        # В Himalayas вакансии лежат в ключе "jobs"
        jobs = data.get("jobs", [])

        logger.info(f"Успешно получено {len(jobs)} вакансий.")
        return jobs

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка сети или API: {e}")
        return []