import os

# Путь к файлу .env
env_file = ".env"

# Если файл .env существует, читаем данные и устанавливаем их как переменные окружения
if os.path.exists(env_file):
    with open(env_file, "r") as file:
        for line in file:
            # Игнорируем пустые строки и строки без знака "="
            if line.strip() and "=" in line:
                # Разделяем ключ и значение по знаку "="
                key, value = line.strip().split("=", 1)  # Используем maxsplit=1, чтобы избежать разделения значений с символами "="
                os.environ[key] = value

# Теперь мы можете использовать переменные окружения в вашем скрипте
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
KEY = os.getenv("KEY")