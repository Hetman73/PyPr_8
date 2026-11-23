import logging
from logger_config import setup_logging
from api_client import fetch_vacancies
from vacancy_filter import process_vacancies
from file_saver import save_to_json

# 1. Включаем логирование
setup_logging()
logger = logging.getLogger(__name__)


def main():
    logger.info("=== Старт программы ===")

    # 2. Параметры поиска
    search_word = "python"
    stop_words = ["senior", "lead", "manager"]

    # 3. Получаем данные
    raw_data = fetch_vacancies(search_word)
    if not raw_data:
        logger.warning("Не удалось получить данные. Завершение.")
        return

    # 4. Фильтруем данные
    filtered_data = process_vacancies(raw_data, stop_words)
    if not filtered_data:
        logger.warning("Все вакансии отфильтрованы. Завершение.")
        return

    # 5. Сохраняем результат
    save_to_json(filtered_data, search_word)
    logger.info("=== Программа завершена успешно ===")


if __name__ == "__main__":
    main()