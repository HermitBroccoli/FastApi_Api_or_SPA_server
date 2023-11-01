from pydantic import BaseModel
from typing import *

class Portsss(BaseModel):
	id: int
	title: Optional[str] = None