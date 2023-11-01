from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import urls
from setting import *

app = FastAPI(
    title=NAME_PROJECT
)

configure_middleware(app, origins)
static_apply(app, paths)

for url in urls:
	app.include_router(url)