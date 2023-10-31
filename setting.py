from app.middleware import *
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import origins, add_url_middleware, configure_middleware

origins =[
	"http://localhost:5173"
]

add_url_middleware(origins)

