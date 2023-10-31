from fastapi import FastAPI, Request, Query, APIRouter

router = APIRouter(
	prefix="/posts"
)

@router.get("/{id}")
async def get_user(id: int):
	return {"id": id}



routers = [router]