import logging

logger = logging.getLogger(__name__)


def process_vacancies(raw_jobs: list, exclude_words: list) -> list:
    """
    Извлекает нужные поля и отсеивает вакансии по стоп-словам.
    """
    logger.info(f"Начинаем фильтрацию. Стоп-слова: {exclude_words}")
    processed = []

    for job in raw_jobs:
        title = job.get("title", "Без названия")

        # Проверяем, есть ли в названии стоп-слово (игнорируя регистр)
        # any() возвращает True, если хотя бы одно слово найдено
        if any(word.lower() in title.lower() for word in exclude_words):
            logger.debug(f"Вакансия '{title}' отсеяна (стоп-слово).")
            continue

        # Извлекаем нужные данные, используя .get() для безопасности
        processed.append({
            "title": title,
            "salary_min": job.get("minSalary"),
            "salary_max": job.get("maxSalary"),
            "url": job.get("applicationLink")
        })

    logger.info(f"После фильтрации осталось {len(processed)} вакансий.")
    return processed