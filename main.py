from app.core.feature.parser import uvicornObj

if __name__ == '__main__':
	import uvicorn
	uvicorn.run("public.index:app", host=uvicornObj["host"], reload=uvicornObj["reload"], port=uvicornObj["port"])