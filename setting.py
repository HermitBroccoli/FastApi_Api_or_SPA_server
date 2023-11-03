from app.middleware import *
from app.core.config import url_middleware, configure_middleware, origins, static
import os

# Бета Основные переменные
# ----------------------------------------------------------------



# ----------------------------------------------------------------

# Основные функции
# ----------------------------------------------------------------
url_middleware([
    "http://localhost:5173"
])  # данная часть добовляет машруты для кросс-доменных запросов front-end

# Бета
middleware = [
    {}
]

# объявление статических файлов
static([
    {"subpath": "/public", "dir": "public", "name": "public"},
    {"subpath": "/assets", "dir": "public\\assets", "name": "assets"},
])
# ----------------------------------------------------------------
