from fastapi import FastAPI, Request, Query, APIRouter, Form, File, UploadFile
from app.models.portsmodel import Portsss
from fastapi.responses import JSONResponse, FileResponse
from typing import Annotated
import os	
from typing import List

from pydantic import BaseModel

router = APIRouter(
	prefix="/posts",
	tags=["posts"],
)

UPLOAD_FOLDER = "storage\\public"

class User(BaseModel):
	login: str
	password: str

@router.post("/post")
async def post_post(login: Annotated[str, Form()], password: Annotated[str, Form()], file: UploadFile):
	return {"login": login, "password": password, "file": {
		"name": file.filename,
		"size": file.size,
		"type": file.content_type
	}}

@router.post("/login")
async def login(files: List[UploadFile]):
	
	for file in files:
		file_path = os.path.join(UPLOAD_FOLDER, file.filename)
		with open(file_path, "wb") as f:
			f.write(file.file.read())
	
	return {"message": "Files uploaded successfully"}

@router.get("/download")
async def download_file(filename: str):
    file_path = os.path.join("storage\\public", filename)
    return FileResponse(file_path, headers={"Content-Disposition": f"attachment; filename={filename}"})

routers = [router]