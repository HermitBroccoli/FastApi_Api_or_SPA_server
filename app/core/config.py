import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
from .routers.errorsPaths import router
from .routers import *
from colorama import init, Fore
import sys

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

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USER = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE_NAME = os.getenv("DB_DATABASE")

# функция проверки ключа
def check_secret_key(_: Optional = None):	
	_KEY = str(os.getenv("APP_KEY", default=''))
	init(autoreset=True)
	if _KEY is None or _KEY == '' or _KEY.replace(" ", "") == '':
		print(Fore.RED + "Отсутвует секретный ключ!")
		os._exit(1)

# Объект кросс-доменных запросов front-end
#-----------------------------------------------------------------------
origins : List[str] = [*DEFAULT_ORIGIN]
#-----------------------------------------------------------------------

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

	check_secret_key()

	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins, 
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	static_apply(app, paths)

	for error_url in error_urls:
		app.add_route(error_url)

#-----------------------------------------------------------------------