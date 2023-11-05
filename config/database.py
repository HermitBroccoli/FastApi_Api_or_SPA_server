from app.core.config import HOST, PORT, USER, PASSWORD, DATABASE_NAME
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Database():
	def __init__(self):
		self.HOST = HOST
		self.PORT = int(PORT)
		self.USER = USER
		self.PASSWORD = PASSWORD
		self.DATABASE_NAME = DATABASE_NAME
	
	def datebase_url(self):
		return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE_NAME}"

class RedisDatabase:
	def __init__(self):
		pass

class Base(DeclarativeBase):
	pass

database = Database()
redis_base = RedisDatabase()