import os
import importlib

# Создайте пустой список для хранения импортированных моделей
imported_models = []

# Укажите путь к папке, где находятся ваши файлы с моделями
models_directory = "app/models"

# Получите список всех файлов .py в указанной папке, исключая __init__.py и models.py
model_files = [f for f in os.listdir(models_directory) if f.endswith(".py") and f != "__init__.py" and f != "models.py"]

for file in model_files:
	module_name = f"app.models.{file[:-3]}"  # Формируем полное имя модуля
	module = importlib.import_module(module_name)
	# Получаем все имена из модуля, кроме имени "__all__", если таковое определено
	model_names = getattr(module, '__all__', [name for name in dir(module) if not name.startswith('_')])
	# Добавляем все найденные имена моделей в список импортированных моделей
	imported_models.extend([getattr(module, model_name) for model_name in model_names])
# Теперь у вас есть список всех импортированных моделей
