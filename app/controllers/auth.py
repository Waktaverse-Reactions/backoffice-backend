from datetime import datetime

from fastapi import Request, status, APIRouter
from fastapi.responses import JSONResponse

from app.common.exceptions import error_code, CloudflareUnauthorizedException
from app.plugins.jwt import JwtPlugin


router = APIRouter(prefix="/auth", tags=["Authentication"])
jwtPlugin = JwtPlugin()


@router.get(
    "/cloudflare/@me",
    summary="Get current user from Cloudflare Access",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def get_cfuser(request: Request):
    try:
        user = await jwtPlugin.get_user(request.headers.get("CF_Authorization"))

        return JSONResponse(
            {
                "code": "OPERATION_COMPLETE",
                "status": status.HTTP_200_OK,
                "data": user,
                "responseAt": datetime.now().isoformat(),
            },
            status_code=status.HTTP_200_OK,
        )
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
