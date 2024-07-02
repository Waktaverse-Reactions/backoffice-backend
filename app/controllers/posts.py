from datetime import datetime
from fastapi import status, APIRouter

from app.common.exceptions import error_code, APIException
from app.controllers.dtos.posts import PostsResponseDto, SpecficPostResponseDto
from app.services.posts import PostsService

router = APIRouter(prefix="/posts", tags=["Post Management"])
postsService = PostsService()


@router.get(
    "/",
    summary="등록된 전체 게시글을 조회합니다.",
    description="Wakre 사이트에 등록된 전체 게시글 리스트를 반환합니다.",
    response_model=PostsResponseDto,
    status_code=status.HTTP_200_OK,
)
async def listPost(page: int = 1, count: int = 12):
    return {
        "code": "OPERATION_COMPLETE",
        "status": 200,
        "data": postsService.getMany(page, count),
        "responseAt": datetime.now().isoformat(),
    }


@router.get(
    "/{id}",
    summary="특정 게시글을 조회합니다.",
    description="Wakre 사이트에 등록된 특정 게시글 정보를 반환합니다.",
    response_model=SpecficPostResponseDto,
    status_code=status.HTTP_200_OK,
)
async def getPost(id: str):
    return {
        "code": "OPERATION_COMPLETE",
        "status": 200,
        "data": postsService.get(id),
        "responseAt": datetime.now().isoformat(),
    }


@router.put(
    "/",
    summary="게시글을 새로 포스트합니다.",
    description="Wakre 사이트에 새로운 게시글을 포스트합니다.",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def newPost():
    raise APIException(
        code=error_code.get(str(status.HTTP_501_NOT_IMPLEMENTED)),
        status=status.HTTP_501_NOT_IMPLEMENTED,
        message="Not implemented yet.",
    )


@router.patch(
    "/{id}",
    summary="등록된 게시글을 수정합니다.",
    description="Wakre 사이트에 이미 등록된 게시글을 수정합니다.",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def updatePost():
    raise APIException(
        code=error_code.get(str(status.HTTP_501_NOT_IMPLEMENTED)),
        status=status.HTTP_501_NOT_IMPLEMENTED,
        message="Not implemented yet.",
    )


@router.delete(
    "/{id}",
    summary="등록된 게시글을 삭제합니다.",
    description="Wakre 사이트에 이미 등록된 게시글을 삭제합니다. 관리자 권한이 필요합니다.",
    response_model=dict,
    status_code=status.HTTP_200_OK,
)
async def deletePost():
    raise APIException(
        code=error_code.get(str(status.HTTP_501_NOT_IMPLEMENTED)),
        status=status.HTTP_501_NOT_IMPLEMENTED,
        message="Not implemented yet.",
    )
