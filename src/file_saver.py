import json
import logging
from datetime import date

logger = logging.getLogger(__name__)


def save_to_json(vacancies: list, search_query: str) -> None:
    """
    Сохраняет список вакансий в JSON-файл с именем, содержащим дату.
    """
    today = date.today().isoformat()  # Получаем дату в формате ГГГГ-ММ-ДД
    # Очищаем запрос от пробелов, чтобы использовать в имени файла
    safe_query = search_query.replace(" ", "_").lower()

    filename = f"{today}_{safe_query}.json"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            # ensure_ascii=False позволяет сохранить русские буквы (если они будут)
            # indent=2 делает файл читаемым
            json.dump(vacancies, f, ensure_ascii=False, indent=2)
        logger.info(f"Данные сохранены в файл: {filename}")
    except IOError as e:
        logger.error(f"Не удалось записать файл: {e}")