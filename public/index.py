from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import urls
from setting import *
from config.app import app_config

app = FastAPI(
    title=app_config.APP_NAME
)

configure_middleware(app, origins) # применение кросс-доменных запросов front-end

for url in urls:
	app.include_router(url)
