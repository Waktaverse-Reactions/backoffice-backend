from typing import Any, Optional
from pydantic import BaseModel

from fastapi import status
from datetime import datetime


class BaseResponseDto(BaseModel):
    code: str = "OPERATION_COMPLETE"
    status: int = status.HTTP_200_OK

    data: Optional[Any]

    responseAt: str = datetime.now().isoformat()


class BasePaginationDto(BaseModel):
    currentPage: int
    totalPage: int
    hasNextPage: bool
