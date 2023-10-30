from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "HEI SERVER"
)



users = [
    {"name": "brocc", "password": "11111111"}
]

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def block_favicon(request: Request, call_next):
    if request.url.path == "/favicon.ico":
        return None  # Возвратите None, чтобы прервать выполнение запроса к favicon.ico
    response = await call_next(request)
    return response

@app.get("/")
async def index():
    return {"message": "Hello World 111"}

@app.get("/test/{id}")
async def test(id: int):
	return {"message": f"Hello World {id}"}
