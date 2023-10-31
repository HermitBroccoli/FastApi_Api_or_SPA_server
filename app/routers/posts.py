from fastapi import FastAPI, Request, Query, APIRouter
from app.models.portsmodel import Portsss

router = APIRouter(
	prefix="/posts"
)

""" @router.post("/post", response_model=Portsss)
async def post_post(post: Portsss):
	return {"id": post.id, "title": post.title} """


routers = [router]