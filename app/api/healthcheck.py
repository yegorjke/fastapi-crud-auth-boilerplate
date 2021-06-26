from fastapi.routing import APIRouter

router = APIRouter(tags=["Debug"])

@router.get("/healthcheck")
async def healthcheck():
    check = True
    return {"healthcheck": check}