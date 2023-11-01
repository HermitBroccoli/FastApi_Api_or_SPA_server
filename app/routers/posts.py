from fastapi import FastAPI, Request, Query, APIRouter, Form
from app.models.portsmodel import Portsss

from typing import Annotated


router = APIRouter(
	prefix="/posts",
	tags=["posts"],
)



@router.post("/post/{id}", response_model=Portsss)
async def post_post(id: int, title: Annotated[str, Form()]):
	return {"id": id, "title": title}


routers = [router]