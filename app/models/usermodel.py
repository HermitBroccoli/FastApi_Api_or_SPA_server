from pydantic import BaseModel
from datetime import date

class User(BaseModel):
	id: int
	name: string
	email: string
	password: string
	creat_at: date
	
