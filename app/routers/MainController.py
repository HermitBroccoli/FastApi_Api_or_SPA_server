from fastapi import FastAPI, Request, Query, APIRouter

router = APIRouter()

@router.get("/")
async def index():
	return {"message": "Hello World"}

""" @router.get("/about")
async def about():
	return {"message": "About Us"} """


routers = [router]