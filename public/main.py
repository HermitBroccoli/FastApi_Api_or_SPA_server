from fastapi import FastAPI
from app.routers import urls
from setting import *

app = FastAPI(
    title="HEI SERVER"
)

configure_middleware(app, origins)

for url in urls:
	app.include_router(url)
