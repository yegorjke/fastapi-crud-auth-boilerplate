from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def index():
    return {"message": "hello world"}

@api.get("/healthcheck")
async def healthcheck():
    check = True
    return {"healthcheck": check}