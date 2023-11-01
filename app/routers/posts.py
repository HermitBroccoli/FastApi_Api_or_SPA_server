from fastapi import FastAPI, Request, Query, APIRouter
from app.models.portsmodel import Portsss

from pydantic import BaseModel

router = APIRouter(
	prefix="/posts",
	tags=["posts"],
)

class User(BaseModel):
	login: str
	password: str

@router.post("/post/{id}", response_model=Portsss)
async def post_post(id: int, title: str):
	return {"id": id, "title": title}

@router.post("/login", response_model=User)
async def login(post: User):
	return {"login": post.login, "password": post.password}


routers = [router]