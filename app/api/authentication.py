from fastapi import HTTPException, status, APIRouter, Request, Response

router = APIRouter(tags=["Authentication"], prefix="/auth")

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(req: Request):
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                        detail={"error_message": "'/login' is not implemented yet!"})

@router.get("/logout", status_code=status.HTTP_200_OK)
async def logout():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                        detail={"error_message": "'/logout' is not implemented yet!"})

@router.post("/signup", status_code=status.HTTP_200_OK)
async def signup():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                        detail={"error_message": "'/singup' is not implemented yet!"})

@router.post("/forgot", status_code=status.HTTP_200_OK)
async def forgot_password():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                        detail={"error_message": "'/forgot_password' is not implemented yet!"})

@router.post("/reset", status_code=status.HTTP_200_OK)
async def reset_password():
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                        detail={"error_message": "'reset_password' is not implemented yet!"})