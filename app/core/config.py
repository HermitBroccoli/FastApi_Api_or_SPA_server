import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
import sys
from typing import Dict, List, Optional

BASE_URL = os.getcwd();

# Объект конфигурации FastAPI для кросс-доменных запросов front-end
#-----------------------------------------------------------------------
DEFAULT_ORIGIN : List[str] = [
	"http://localhost",
	"http://localhost:8080",
]
#-----------------------------------------------------------------------

# Бета
#-----------------------------------------------------------------------
PATH_STATIC : List[Dict] = []
#-----------------------------------------------------------------------

# Путь к файлу .env
#-----------------------------------------------------------------------
env_file = ".env"

# Если файл .env существует, читаем данные и устанавливаем их как переменные окружения
def envripoint(_: Optional = None):
	if os.path.exists(env_file):
		with open(env_file, "r") as file:
			for line in file:
				# Игнорируем пустые строки и строки без знака "="
				if line.strip() and "=" in line:
					# Разделяем ключ и значение по знаку "="
					key, value = line.strip().split("=", 1)  # Используем maxsplit=1, чтобы избежать разделения значений с символами "="
					os.environ[key] = value
#-----------------------------------------------------------------------

# Перезагрузка конфигурации перемены окружения и их объявления
#-----------------------------------------------------------------------
envripoint("сюда ничего не вносим")
#-----------------------------------------------------------------------

# Класса для получение объекта конфигурации базы данных
#-----------------------------------------------------------------------
class DatabaseConfig:
	_db_host = str(os.getenv("DB_HOST"))
	_db_user = str(os.getenv("DB_USER"))
	_db_password = str(os.getenv("DB_PASSWORD"))
	_db_port_str = os.getenv("DB_PORT")

	if _db_port_str and _db_port_str.isdigit():
		_db_port = int(_db_port_str)
	else:
		_db_port = 5432

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
#-----------------------------------------------------------------------

class RedisDatabase:
	_redic_host = str(os.getenv("REDIS_HOST"))
	_redic_port_str = os.getenv("REDIS_PORT")

	if _redic_port_str and _redic_port_str.isdigit():
		_redic_port = int(_redic_port_str)

	_redic_password = str(os.getenv("REDIS_PASSWORD"))

# Конфигурация базы данных
#-----------------------------------------------------------------------
CONFIG = DatabaseConfig.config_collection()
#-----------------------------------------------------------------------

# Получить секретный ключ
#-----------------------------------------------------------------------
def secret_key(_: Optional = None):
	return str(os.getenv("KEY"))
#-----------------------------------------------------------------------

# Получить название проекта
#-----------------------------------------------------------------------
def title(title: Optional[str] = None):
	if title is None:
		return str(os.getenv("APP_NAME"))
	else:
		return str(title)
#-----------------------------------------------------------------------

# Объект кросс-доменных запросов front-end
#-----------------------------------------------------------------------
origins : List[str] = [*DEFAULT_ORIGIN]
#-----------------------------------------------------------------------

APP_URL = str(os.getenv("APP_URL", "http://localhost"))

# Бета
#-----------------------------------------------------------------------
# allow_or_rex = []
#-----------------------------------------------------------------------

# Бета
#-----------------------------------------------------------------------
paths : List[Dict] = [*PATH_STATIC]

def static(pathss: List[str]):
	for path in pathss:
		paths.append({"subpath": path["subpath"], "dir": path["dir"], "name": path["name"]})

def static_apply(app: FastAPI,arr: List[Dict]):
	for path in arr:
		app.mount(str(path["subpath"]), StaticFiles(directory=str(path["dir"])), name=path["name"])

#-----------------------------------------------------------------------

# добовляет машруты для кросс-доменных запросов front-end
#-----------------------------------------------------------------------
def url_middleware(urls: List[str]) -> List[str]:
	origins.extend(urls)
#-----------------------------------------------------------------------

# Бета
#-----------------------------------------------------------------------
""" def path_files():
	pass """
#-----------------------------------------------------------------------	

# кононфигурация FastAPI для кросс-доменных запросов front-end
#-----------------------------------------------------------------------
def configure_middleware(app: FastAPI, origins: List[str]):
	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins, 
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
#-----------------------------------------------------------------------