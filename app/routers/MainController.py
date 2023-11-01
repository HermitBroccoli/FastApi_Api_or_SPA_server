from fastapi import FastAPI, Request, Query, APIRouter
from fastapi.responses import FileResponse
import os

current_dir = os.getcwd()
path = os.path.join(current_dir, "public\\favicon.gif")

router = APIRouter()

@router.get("/")
async def index():
	return {"message": "Hello World"}

@router.get("/about")
async def about():
	return {"message": "About Us"}

@router.get("/favicon.ico")
async def favicon():
	return FileResponse(path, media_type="image/gif")

@router.get("/show_image")
async def show_image():
    return FileResponse("static/favicon.gif", media_type="image/gif")

routers = [router]