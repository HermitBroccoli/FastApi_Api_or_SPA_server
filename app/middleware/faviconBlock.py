from fastapi import Request

async def block_favicon(request: Request, call_next):
	if request.url.path == "/favicon.i co":
		return None  # Возвратите None, чтобы прервать выполнение запроса к favicon.ico
	response = await call_next(request)
	return response