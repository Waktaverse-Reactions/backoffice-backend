from app.common.dtos.base import BaseResponseDto
from app.plugins.jwt import CloudflareJwtDto


class CloudflareUserResponseDto(BaseResponseDto):
    data: CloudflareJwtDto
