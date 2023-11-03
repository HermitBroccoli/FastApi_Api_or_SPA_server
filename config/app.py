import os
from app.core.feature.parser import uvicornObj

class ApplicationConfig:
	def __init__(self):
		self.APP_NAME = os.getenv("APP_NAME", default="FastApi")
		self.KEY = os.getenv("APP_KEY")
		self.DEBUG = os.getenv("APP_DEBUG", default=True)
		self.APP_URL = uvicornObj

app_config = ApplicationConfig()