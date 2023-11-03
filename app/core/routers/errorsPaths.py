from fastapi import APIRouter

router = APIRouter(
	prefix="/errors",
	tags=["Errors"]
)

@router.get("/404", include_in_schema=True)
def error_404():
	return {'status': 404}


routers = [router]