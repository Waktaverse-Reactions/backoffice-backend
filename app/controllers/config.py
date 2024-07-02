from fastapi import status, APIRouter
from app.common.exceptions import error_code, APIException
from app.controllers.dtos.root import RootResponseDto

router = APIRouter(prefix="/config", tags=["Personalized Configuration"])


@router.get("/", response_model=dict, status_code=status.HTTP_200_OK)
async def config():
    raise APIException(
        code=error_code.get(str(status.HTTP_501_NOT_IMPLEMENTED)),
        status=status.HTTP_501_NOT_IMPLEMENTED,
        message="Not implemented yet.",
    )
