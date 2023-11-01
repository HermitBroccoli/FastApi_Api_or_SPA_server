import os
import importlib

# Создайте пустой массив для хранения URL-ов
urls = []

# Укажите путь к папке, где находятся ваши файлы с модулями
router_directory = "app/routers"

# Получите список всех файлов .py в указанной папке, исключая __init__.py
router_files = [f for f in os.listdir(router_directory) if f.endswith(".py") and f != "__init__.py"]

for file in router_files:
    module_name = f"app.routers.{file[:-3]}"  # Формируем полное имя модуля
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, 'routers'):
            urls.extend(module.routers)
    except ImportError:
        pass
