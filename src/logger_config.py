import logging
import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()


def setup_logging():
    # Получаем уровень логирования из переменной окружения (по умолчанию INFO)
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, log_level, logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)
    logger.info(f"Логирование успешно настроено. Текущий уровень: {log_level}")

    return logger


if __name__ == "__main__":
    setup_logging()