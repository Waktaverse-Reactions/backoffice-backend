from datetime import datetime

from fastapi import Request, status, APIRouter
from fastapi.responses import JSONResponse

from app.common.exceptions import APIException, error_code, CloudflareUnauthorizedException
from app.controllers.dtos.auth import CloudflareUserResponseDto
from app.plugins.jwt import JwtPlugin


router = APIRouter(prefix="/auth", tags=["Authentication"])
jwtPlugin = JwtPlugin()


@router.get(
    "/cloudflare/@me",
    summary="Cloudflare Access를 이용해 로그인합니다.",
    description="Cloudflare Access를 이용해 로그인하고, 사용자 정보를 조회합니다.",
    response_model=CloudflareUserResponseDto,
    status_code=status.HTTP_200_OK,
)
async def get_cfuser(request: Request):
    try:
        user = await jwtPlugin.get_user(request.headers.get("CF_Authorization"))

        return {
            "code": "OPERATION_COMPLETE",
            "status": status.HTTP_200_OK,
            "data": user,
            "responseAt": datetime.now().isoformat(),
        }
    except CloudflareUnauthorizedException:
        return JSONResponse(
            {
                "code": error_code.get(str(status.HTTP_401_UNAUTHORIZED)),
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "로그인 토큰이 만료되었거나 올바르지 않은 접근입니다.",
                "responseAt": datetime.now().isoformat(),
            },
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@router.get(
    "/navercafe/@me",
    summary="네이버 카페 연동 상태를 조회합니다.",
    description="네이버 카페 연동 상태를 조회하고, 필요한 경우 다시 로그인합니다.",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def get_naveruser(request: Request):
    raise APIException(
        code=error_code.get(str(status.HTTP_501_NOT_IMPLEMENTED)),
        status=status.HTTP_501_NOT_IMPLEMENTED,
        message="Not implemented yet.",
    )
