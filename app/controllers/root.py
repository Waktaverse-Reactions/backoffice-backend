from fastapi import status, APIRouter
from app.controllers.dtos.root import RootResponseDto

router = APIRouter(tags=["Health Checker"])


@router.get("/", response_model=RootResponseDto, status_code=status.HTTP_200_OK)
async def root():
    return {"happy": "hacking"}
