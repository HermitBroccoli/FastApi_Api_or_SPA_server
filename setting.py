from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import title, secret_key, url_middleware, configure_middleware, origins, DatabaseConfig, static, static_apply, paths
import os

# Основные переменные
#----------------------------------------------------------------
NAME_PROJECT = title() # Название проекта
SECRET_KEY = secret_key(165213613) # Секретный ключ
DATABASE = DatabaseConfig.config_collection() # Конфигурация базы данных


#----------------------------------------------------------------

# Основные функции
#----------------------------------------------------------------
url_middleware([
	"http://localhost:5173"
]) # данная часть добовляет машруты для кросс-доменных запросов front-end

# Бета
middleware = [
	{}
]

# объявление статических файлов
static([
	{"subpath": "/static", "dir": "public", "name": "static"},
])
#----------------------------------------------------------------


