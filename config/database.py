import os

class Database():
	def __init__(self):
		self.HOST = str(os.getenv("DB_HOST", default="localhost"))
		self.PORT = int(os.getenv("DB_PORT", default=5432))
		self.USER = str(os.getenv("DB_USER", default="postgres"))
		self.PASSWORD = str(os.getenv("DB_PASSWORD", "postgres"))
		self.DATABASE_NAME = str(os.getenv("DB_DATABASE", "postgres"))

class RedisDatabase:
	def __init__(self):
		pass

database = Database()