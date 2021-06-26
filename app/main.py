from fastapi import FastAPI

# routers
from .api import healthcheck, authentication


app = FastAPI()
app.include_router(healthcheck.router)
app.include_router(authentication.router)