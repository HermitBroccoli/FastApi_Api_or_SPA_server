from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import title, secret_key, url_middleware, configure_middleware, origins, DatabaseConfig


# Основные переменные
#----------------------------------------------------------------
NAME_PROJECT = title() # Название проекта
SECRET_KEY = secret_key() # Секретный ключ
CONFIG = DatabaseConfig.config_collection() # Конфигурация базы данных


#----------------------------------------------------------------

# Основные функции
#----------------------------------------------------------------
url_middleware([
	"http://localhost:5173"
]) # данная часть добовляет машруты для кросс-доменных запросов front-end



#----------------------------------------------------------------


