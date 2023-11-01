from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import urls
from setting import *

app = FastAPI(
    title=NAME_PROJECT
)

configure_middleware(app, origins) # применение кросс-доменных запросов front-end

static_apply(app, paths) # применение статических файлов

for url in urls:
	app.include_router(url)