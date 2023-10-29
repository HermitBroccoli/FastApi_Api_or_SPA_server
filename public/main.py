from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title = "HEI SERVER"
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
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
    return {"message": "Hello World"}