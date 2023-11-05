from config.database import Base
from sqlalchemy import *
from sqlalchemy.sql import func

class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(255), nullable=False)
        login = Column(String(255), nullable=False)
        password = Column(String(255), nullable=False)
        create_at = Column(DateTime, nullable=False, default=func.now())
        updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
        is_superuser = Column(Boolean, default=False)
        is_active = Column(Boolean, default=True)

__all__ = ['User']