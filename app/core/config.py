import os
from fastapi import FastAPI
from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
import sys
from app.middleware import *

DEFAULT_ORIGIN = [
	"http://localhost",
	"http://localhost:8080",
]

PATHS = {
	"static": os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"),
    "templates": os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
}

# Путь к файлу .env
env_file = ".env"

# Если файл .env существует, читаем данные и устанавливаем их как переменные окружения
def envripoint():
	if os.path.exists(env_file):
		with open(env_file, "r") as file:
			for line in file:
				# Игнорируем пустые строки и строки без знака "="
				if line.strip() and "=" in line:
					# Разделяем ключ и значение по знаку "="
					key, value = line.strip().split("=", 1)  # Используем maxsplit=1, чтобы избежать разделения значений с символами "="
					os.environ[key] = value

envripoint()

# Класса для получение объекта конфигурации базы данных
class DatabaseConfig:
	_db_host = str(os.getenv("DB_HOST"))
	_db_user = str(os.getenv("DB_HOST_USER"))
	_db_password = str(os.getenv("DB_HOST_PASSWORD"))
	_db_port_str = os.getenv("DB_HOST_PORT")

	if _db_port_str and _db_port_str.isdigit():
		_db_port = int(_db_port_str)
	else:
		print("Error: Invalid DB_HOST_PORT value:", _db_port_str)
		sys.exit(1)  # Остановить программу с кодом ошибки 1

	_db_name = str(os.getenv("DB_HOST_NAME"))

	@classmethod
	def config_collection(cls):
		return {
			"host": cls._db_host,
			"user": cls._db_user,
			"password": cls._db_password,
			"port": cls._db_port,
			"name": cls._db_name
		}

CONFIG = DatabaseConfig.config_collection()


# Теперь мы можете использовать переменные окружения в вашем скрипте
def secret_key():
	return str(os.getenv("KEY"))

def title():
	return str(os.getenv("NAME_PROJECT"))

origins = [*DEFAULT_ORIGIN]

allow_or_rex = []

def url_middleware(urls):
	origins.extend(urls)

def path_files():
	pass
	

def configure_middleware(app: FastAPI, origins):
	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins, 
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	""" # Получение всех функций middleware из папки
	middlewares = [middleware for _, middleware in locals().items() if callable(middleware) and middleware.__module__.startswith('app.middleware.')]

	# Применение всех middleware
	for middleware in middlewares:
		app.middleware("http")(middleware) """