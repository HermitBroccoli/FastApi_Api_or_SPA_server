import uvicorn
from app.core.feature.parser import uvicornObj as raw

def start():
	# track_and_restart_uvicorn_on_env_change(".env", "main.py")
	uvicorn.run("public.index:app", host=raw["host"], port=raw["port"], reload=raw["reload"], log_level=raw["log_level"])

if __name__ == "__main__":
	start()