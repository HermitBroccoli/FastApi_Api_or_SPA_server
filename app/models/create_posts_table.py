from config.database import Base
from sqlalchemy import *
from sqlalchemy.sql import func

class Posts(Base):
		__tablename__ = "posts"
		id = Column(Integer, primary_key=True, autoincrement=True)
		title = Column(String(255), nullable=False)
		body = Column(String(255), nullable=False)
		create_at = Column(DateTime, nullable=False, default=func.now())
		updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

__all__ = ['Posts']